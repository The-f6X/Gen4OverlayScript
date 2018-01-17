#!/usr/bin/env python3
import argparse
import shutil
import sys
import time
from collections import namedtuple
from enum import Enum, IntEnum, EnumMeta
from typing import Any, List, TextIO

import numpy
from matplotlib import pyplot
from matplotlib.pyplot import clf as clear_figures

PokeNamespace = namedtuple('PokeNamespace', ['input', 'assets', 'output', 'verbosity', 'silent'])


################################################################################
# region SimpleLogger
################################################################################

class SimpleLogger:
    class Level(IntEnum):
        SILENT = -2
        ERROR = -1
        WARN = 0
        INFO = 1
        DEBUG = 2

    def __init__(self, log_level: Level = Level.INFO):
        if log_level > max(self.Level):
            log_level = max(self.Level)
        self._log_state = log_level

    def debug(self, msg: str):
        self._emit(msg, self.Level.DEBUG)

    def error(self, msg: str):
        self._emit(msg, self.Level.ERROR)

    def info(self, msg: str):
        self._emit(msg, self.Level.INFO)

    def warn(self, msg: str):
        self._emit(msg, self.Level.WARN)

    def _emit(self, msg: str, level: Level):
        if level <= self._log_state:
            print(f'{time.strftime("%H:%M:%S")} [{level.name}] {msg}', file=sys.stderr)


# endregion

################################################################################
# region StatusCondition
################################################################################

class _StatusConditionMeta(EnumMeta):
    def __call__(cls, value, *args, **kwargs):
        if value in range(1, 8):  # handles sleep state edge case
            value = 1             # normalizes multiple values for sleep to the actual value
        return super().__call__(value, *args, **kwargs)


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
    X_ARRAY: numpy.ndarray = numpy.arange(1)

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
        poke_dict = dict(map(
                lambda x: (x[0], int(x[1])),
                pairs))

        return Pokemon(pokedex_id=int(pairs[0][1]),  # getting by index instead of trying to match PKM1, PKM2, etc
                       cur_hp=poke_dict['HP'],
                       max_hp=poke_dict['MAXHP'],
                       level=poke_dict['Lvl'],
                       egg=bool(poke_dict['Egg']),
                       status=StatusCondition(poke_dict['Status']))

    def inactive(self) -> bool:
        return self.is_egg or self.id == 0

    def emit(self) -> str:
        level = 'N/A' if self.inactive() else self.level
        hp = 'N/A' if self.inactive() else f'{self.cur_hp}/{self.max_hp}'
        if self.is_egg:
            status = 'Egg'
        elif self.id == 0:
            status = 'Empty'
        else:
            status = self.status

        return f'Lvl: {level}\nHP: {hp}\nStatus: {status}'

    def empty(self) -> bool:
        return self.id == 0

    def render_health(self, out_path: str):
        clear_figures()
        health_percent = self.cur_hp / self.max_hp

        if health_percent > 0.5:
            hp_color = '#4CAF50'  # green
        elif 0.25 < health_percent <= 0.5:
            hp_color = '#FFC107'  # yellow
        else:
            hp_color = '#F44336'  # red

        pyplot.barh(Pokemon.X_ARRAY, self.cur_hp, color=hp_color)

        # background
        pyplot.barh(
                Pokemon.X_ARRAY,
                self.max_hp - self.cur_hp,
                left=self.cur_hp,
                color='#212121')

        pyplot.axis('off')

        pyplot.savefig(
                out_path,
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

def _fetch_raw_team(handle: TextIO) -> str:
    return handle.read().strip()


def _parse_team(raw_team: str) -> List[Pokemon]:
    lines = raw_team.splitlines()
    filtered: List[str] = list(filter(bool, lines))
    evens = filtered[::2]
    return list(map(Pokemon.from_tpp_string, evens))


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
                        help='silences the script - no output at all')
    return parser.parse_args()


def main():
    config = _parse_config()
    team_path = config.input
    assets_dir = config.assets
    output_dir = config.output
    log_level = SimpleLogger.Level.SILENT if config.silent else config.verbosity + 1
    log = SimpleLogger(log_level)
    saved_state = ''

    log.info('The_F6X overlay loop running!')
    while True:
        try:
            team_file = open(team_path)
        except FileNotFoundError:
            log.warn(f'teamfile not found at {team_path}, trying again...')
            continue

        time.sleep(1)
        fresh_state = _fetch_raw_team(team_file)
        if not fresh_state or fresh_state == saved_state:
            log.debug('teamfile unchanged since last loop, skipping')
            continue
        team = _parse_team(fresh_state)
        saved_state = fresh_state

        for i in range(len(team)):
            pokemon = team[i]
            party_image = f'{output_dir}__party{i + 1}.png'

            if pokemon.is_egg:
                shutil.copyfile(src=f'{assets_dir}egg.png',
                                dst=party_image)
            else:
                shutil.copyfile(src=f'{assets_dir}{pokemon.id}.png',
                                dst=party_image)

            with open(f'{output_dir}HP{i + 1}.txt', mode='w') as text_file:
                text_file.write(pokemon.emit())

            healthbar_path = f'{output_dir}health{i + 1}.png'
            if pokemon.empty():
                shutil.copyfile(src=f'{assets_dir}Blank.png',
                                dst=healthbar_path)
            else:
                pokemon.render_health(healthbar_path)


# endregion

if __name__ == '__main__':
    main()
