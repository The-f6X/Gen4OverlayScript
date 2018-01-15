#!/usr/bin/env python3
import shutil
import time
from io import TextIOWrapper

import numpy
from matplotlib import pyplot
from matplotlib.pyplot import clf as clear_figures

X_ARRAY: numpy.ndarray = numpy.arange(1)
TEAM_PATH = 'team.txt'


# TODO replace this with a StatusCondition enum, if possible
def condition_from_int(state: int) -> str:
    status = ''
    if state == 0:
        status = 'Healthy'
    elif state in range(1, 7):  # this is going to give us some trouble
        status = 'Sleep'
    elif state == 8:
        status = 'Poisoned'
    elif state == 16:
        status = 'Burned'
    elif state == 32:
        status = 'Frozen'
    elif state == 64:
        status = 'Paralyzed'
    elif state == 128:
        status = 'Toxic'

    return status


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
                status = 'Fainted'
            else:
                status = condition_from_int(int(lst7[1]))
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


def main():
    saved_state = ''
    while True:
        team_file = open(TEAM_PATH)
        fresh_state = fetch_raw_team(team_file)
        if not fresh_state or fresh_state == saved_state:
            continue
        team = parse_team(fresh_state)
        saved_state = fresh_state

        try:
            for i in range(6):  # TODO technically we shouldn't assume 6 pokemon all the time
                shutil.copyfile(
                        src=f'C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\{team[i][0]}.png',
                        dst=f'C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party{i + 1}.png')

                status_text = f'Lvl: {team[i][3]}\n' + \
                              f'HP: {team[i][1]}/{team[i][2]}\n' + \
                              f'Status: {team[i][4]}'
                
                with open(f'HP{i + 1}.txt', mode='w') as text_file:
                    text_file.write(status_text)

                if team[i][2] == 'A':
                    shutil.copyfile(
                            src='C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png',
                            dst=f'C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health{i + 1}.png')
                else:
                    make_plot(
                            max_hp=team[i][2],
                            current_hp=team[i][1],
                            out_path=f'health{i + 1}.png')
        except Exception:  # TODO narrow down exception or remove the need for try/except here
            pass

        time.sleep(1)

if __name__ == '__main__':
    main()
