#!/usr/bin/env python3
import argparse
import shutil
import sys
import time
from enum import Enum, IntEnum, EnumMeta
from io import TextIOWrapper

import numpy
from matplotlib import pyplot
from matplotlib.pyplot import clf as clear_figures

X_ARRAY: numpy.ndarray = numpy.arange(1)


################################################################################
# SimpleLogger.py
################################################################################

class SimpleLogger:
    class LogState(IntEnum):
        SILENT = -2
        ERROR = -1
        INFO = 0
        WARN = 1
        DEBUG = 2

    def __init__(self, log_state: LogState = LogState.INFO):
        self._log_state = log_state

    def debug(self, msg: str):
        self._emit(f'[DEBUG] {msg}', self.LogState.DEBUG)

    def error(self, msg: str):
        self._emit(f'[ERROR] {msg}', self.LogState.ERROR)

    def info(self, msg: str):
        self._emit(f'[INFO] {msg}', self.LogState.INFO)

    def warn(self, msg: str):
        self._emit(f'[WARN] {msg}', self.LogState.WARN)

    def _emit(self, msg: str, state: LogState):
        if state <= self._log_state:
            print(msg, file=sys.stderr)


################################################################################
# StatusCondition.py
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


################################################################################
# Script.py
################################################################################

def fetch_raw_team(handle: TextIOWrapper) -> str:
    return handle.read().strip()


def parse_team(raw_team: str) -> list:
    team = []
    parse_state = 0

    for entry in raw_team.split('\n'):
        line = entry.strip()
        if parse_state == 0:
            lst = line.split(',')
            lst2 = lst[0].split(' = ')
            lst3 = lst[2].split(' = ')
            lst4 = lst[3].split(' = ')
            lst6 = lst[4].split(' = ')
            lst7 = lst[5].split(' = ')
            lst8 = lst[6].split(' = ')
            name = int(lst2[1])
            health = int(lst3[1])
            max_hp = int(lst4[1])
            level = int(lst6[1])
            if int(name) == 0:
                status = 'Empty'
                health = 'N'
                max_hp = 'A'
                level = 'N/A'
            elif int(lst8[1]) == 1:
                name = 'egg'
                status = 'Egg'
                health = 'N'
                max_hp = 'A'
                level = 'N/A'
            elif int(lst3[1]) == 0:
                status = StatusCondition.FAINTED
            else:
                status = StatusCondition(int(lst7[1]))
            pokemon = [name, health, max_hp, level, status]
            team.append(pokemon)
        if parse_state == 2:
            parse_state = -1
        parse_state += 1
    return team


def make_plot(max_hp: int, current_hp: int, out_path: str):
    clear_figures()
    health_percent = current_hp / max_hp
    bar_height = 50 / 96  # TODO make configurable or just less magic

    if health_percent > 0.5:
        hp_color = '#4CAF50'  # green
    elif 0.25 < health_percent <= 0.5:
        hp_color = '#FFC107'  # yellow
    else:
        hp_color = '#F44336'  # red

    pyplot.barh(X_ARRAY, current_hp, color=hp_color, height=bar_height)

    # background
    pyplot.barh(
            X_ARRAY,
            max_hp - current_hp,
            left=current_hp,
            color='#212121',
            height=bar_height)

    pyplot.axis('off')

    pyplot.savefig(
            out_path,
            bbox_inches='tight',
            pad_inches=0,
            transparent=True,
            dpi=96)


def parse_config() -> argparse.Namespace:
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
    config = parse_config()
    team_path = config.input
    assets_dir = config.assets
    output_dir = config.output
    log_level = SimpleLogger.LogState.SILENT if config.silent else config.verbosity
    log = SimpleLogger(log_level)
    saved_state = ''

    log.info('The_F6X overlay loop running!')
    while True:
        try:
            team_file = open(team_path)
        except FileNotFoundError:
            log.warn(f'teamfile not found at {team_path}, trying again...')
            continue

        fresh_state = fetch_raw_team(team_file)
        if not fresh_state or fresh_state == saved_state:
            continue
        team = parse_team(fresh_state)
        saved_state = fresh_state

        for i in range(6):  # TODO technically we shouldn't assume 6 pokemon all the time
            shutil.copyfile(
                    src=f'{assets_dir}{team[i][0]}.png',
                    dst=f'{output_dir}__party{i + 1}.png')

            status_text = f'Lvl: {team[i][3]}\n' + \
                          f'HP: {team[i][1]}/{team[i][2]}\n' + \
                          f'Status: {team[i][4]}'

            with open(f'{output_dir}HP{i + 1}.txt', mode='w') as text_file:
                text_file.write(status_text)

            if team[i][2] == 'A':  # TODO add these states to an enum or something
                shutil.copyfile(
                        src=f'{assets_dir}Blank.png',
                        dst=f'{output_dir}health{i + 1}.png')
            else:
                make_plot(
                        max_hp=team[i][2],
                        current_hp=team[i][1],
                        out_path=f'{output_dir}health{i + 1}.png')

        time.sleep(1)


if __name__ == '__main__':
    main()
