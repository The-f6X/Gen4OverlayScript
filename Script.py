#!/usr/bin/env python3
import argparse
import logging
import shutil
import time
from collections import namedtuple
from enum import Enum, EnumMeta
from typing import Any, Dict, List, TextIO

from matplotlib import pyplot
from matplotlib.pyplot import clf as clear_figures

PokeNamespace = namedtuple('PokeNamespace', ['input', 'assets', 'output', 'verbosity', 'silent'])


################################################################################
# region StatusCondition
################################################################################

class _StatusConditionMeta(EnumMeta):
    SLEEP_RANGE = range(1, 8)

    def __call__(cls, value, *args, **kwargs):
        if value in cls.SLEEP_RANGE:  # handles sleep state edge case
            value = 1                 # normalizes multiple values for sleep to the enum value
        return super().__call__(value, *args, **kwargs)

    def __contains__(self, item):
        if isinstance(item, int):
            return item in self.SLEEP_RANGE or item in {entry.value for entry in StatusCondition}
        return super(_StatusConditionMeta, self).__contains__(item)


class StatusCondition(Enum, metaclass=_StatusConditionMeta):
    FAINTED = -1
    HEALTHY = 0
    SLEEP = 1
    POISONED = 8
    BURNED = 16
    FROZEN = 32
    PARALYZED = 64
    TOXIC = 128

    def __str__(self):
        return self.name.title()


# endregion

################################################################################
# region Pokemon
################################################################################

class Pokemon:
    HP_BACKGROUND = '#212121'
    HP_GREEN = '#4CAF50'
    HP_YELLOW = '#FFC107'
    HP_RED = '#F44336'

    def __init__(self,
                 pokedex_id: int,
                 cur_hp: int,
                 max_hp: int,
                 level: int,
                 egg: bool,
                 status: StatusCondition):
        self.id = pokedex_id
        self.cur_hp = cur_hp
        self.max_hp = max_hp
        self.level = level
        self.is_egg = egg

        if cur_hp == 0:
            self.status = StatusCondition.FAINTED
        else:
            self.status = status

    @staticmethod
    def from_tpp_string(string: str) -> 'Pokemon':
        pairs = [attr.replace(' ', '').split('=') for attr in string.split(',')]
        try:
            poke_dict: Dict[str, int] = {pair[0]: int(pair[1]) for pair in pairs}

            status = poke_dict['Status']
            if status not in StatusCondition:
                logging.warning(f'emulator yielded out of range value for status: {status}')
                status = 0

            return Pokemon(pokedex_id=int(pairs[0][1]),  # getting by index instead of trying to match PKM1, PKM2, etc
                           cur_hp=poke_dict['HP'],
                           max_hp=poke_dict['MAXHP'],
                           level=poke_dict['Lvl'],
                           egg=bool(poke_dict['Egg']),
                           status=StatusCondition(status))
        except (AttributeError, ValueError):
            logging.critical(f'failed to parse pokemon data, dumping:\n\n{string}\n\n{pairs}\n')
            raise

    def render(self, index: int, assets_dir: str, output_dir: str):
        party_image = f'{output_dir}__party{index + 1}.png'

        if self.is_egg:
            shutil.copyfile(src=f'{assets_dir}egg.png',
                            dst=party_image)
        else:
            shutil.copyfile(src=f'{assets_dir}{self.id}.png',
                            dst=party_image)

        with open(f'{output_dir}HP{index + 1}.txt', mode='w') as text_file:
            text_file.write(self._emit())

        healthbar_path = f'{output_dir}health{index + 1}.png'
        if self._empty():
            shutil.copyfile(src=f'{assets_dir}Blank.png',
                            dst=healthbar_path)
        else:
            self._render_health(healthbar_path)

    def _emit(self) -> str:
        level = 'N/A' if self._inactive() else self.level
        hp = 'N/A' if self._inactive() else f'{self.cur_hp}/{self.max_hp}'
        if self.is_egg:
            status = 'Egg'
        elif self.id == 0:
            status = 'Empty'
        else:
            status = self.status

        return f'Lvl: {level}\nHP: {hp}\nStatus: {status}'

    def _empty(self) -> bool:
        return self.id == 0

    def _inactive(self) -> bool:
        return self.is_egg or self.id == 0

    def _render_health(self, out_path: str):
        clear_figures()
        total_width = 10
        health_percent = self.cur_hp / self.max_hp

        if health_percent > 0.5:
            hp_color = self.HP_GREEN
        elif 0.25 < health_percent <= 0.5:
            hp_color = self.HP_YELLOW
        else:
            hp_color = self.HP_RED

        pyplot.barh(y=0,
                    width=total_width,
                    color=self.HP_BACKGROUND)

        fill_width = health_percent * total_width
        pyplot.barh(y=0,
                    width=fill_width,
                    color=hp_color)

        pyplot.axis('off')

        pyplot.savefig(out_path,
                       bbox_inches='tight',
                       pad_inches=0,
                       transparent=True,
                       dpi=96)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Pokemon):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))


# endregion

################################################################################
# region Script
################################################################################

def _parse_config() -> PokeNamespace:
    parser = argparse.ArgumentParser(
            description="""
            The_F6X's Pokemon Overlay Script. will read teamfile from `./team.txt` by default.""")
    parser.add_argument('-i', '--input',
                        help='path to input teamfile',
                        default='team.txt')
    parser.add_argument('-a', '--assets',
                        help='path to assets directory',
                        default='assets/')
    parser.add_argument('-o', '--output',
                        help='path to output directory',
                        default='out/')
    parser.add_argument('-v', '--verbosity',
                        action='count',
                        default=0,
                        help='increase output verbosity')
    parser.add_argument('-S', '--silent',
                        action='store_true',
                        help='silences the script - no output except for criticals and stack traces')
    return parser.parse_args()


class Overlay:
    def __init__(self, config: PokeNamespace):
        self._assets_dir = config.assets
        self._output_dir = config.output
        self._saved_state = ''
        self._slots: List[Pokemon] = [None for _ in range(6)]  # technically List<Pokemon?>
        self._team_path = config.input

    def run_forever(self):
        logging.info('Overlay loop running!')
        while True:
            try:
                team_file = open(self._team_path)
            except FileNotFoundError:
                logging.warning(f'teamfile not found at {self._team_path}, trying again...')
                continue

            fresh_state = self._fetch_raw_team(team_file)
            if not fresh_state:
                logging.debug('teamfile empty, skipping update')
                continue
            time.sleep(1)
            if fresh_state == self._saved_state:
                logging.debug('teamfile unchanged since last loop, skipping')
                continue
            team = self._parse_team(fresh_state)
            self._saved_state = fresh_state

            for i in range(len(self._slots)):
                if self._slots[i] != team[i]:
                    logging.info(f'slot {i} changed, updating')
                    self._slots[i] = team[i]
                    team[i].render(i, self._assets_dir, self._output_dir)

    @staticmethod
    def _fetch_raw_team(handle: TextIO) -> str:
        return handle.read().strip()

    @staticmethod
    def _parse_team(raw_team: str) -> List[Pokemon]:
        lines = raw_team.splitlines()
        filtered: List[str] = list(filter(bool, lines))
        evens = filtered[::2]
        return [Pokemon.from_tpp_string(item) for item in evens]


# endregion

if __name__ == '__main__':
    params = _parse_config()
    if params.silent:
        log_level = logging.CRITICAL
    elif params.verbosity:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%H:%M:%S',
                        level=log_level)
    Overlay(params).run_forever()
