# cd C:\Users\Daniel\Pictures\Twitch\NDSRead
# python Script.py
import sys
import shutil
import time
import os
from io import TextIOWrapper

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1)
TEAM_PATH = 'team.txt'


def fetch_raw_team(handle: TextIOWrapper) -> str:
    return handle.read().strip()


def parse_team(raw_team: str) -> list:
    team = []
    counter = 0
    Status = ''

    for entry in raw_team.split('\n'):
        line = entry.strip()
        if counter == 0:
            lst = line.split(',')
            lst2 = lst[0].split(' = ')
            lst3 = lst[2].split(' = ')
            lst4 = lst[3].split(' = ')
            lst6 = lst[4].split(' = ')
            lst7 = lst[5].split(' = ')
            lst8 = lst[6].split(' = ')
            name = int(lst2[1])
            HP = int(lst3[1])
            Max_HP = int(lst4[1])
            Level = int(lst6[1])
            if int(name) == 0:
                Status = "Empty"
                HP = "N"
                Max_HP = "A"
                Level = "N/A"
            elif int(lst8[1]) == 1:
                name = "egg"
                Status = "Egg"
                HP = "N"
                Max_HP = "A"
                Level = "N/A"
            elif int(lst3[1]) == 0:
                Status = "Fainted"
            elif int(lst7[1]) == 0:
                Status = "Healthy"
            elif int(lst7[1]) in range(1, 7):
                Status = "Sleep"
            elif int(lst7[1]) == 8:
                Status = "Poisoned"
            elif int(lst7[1]) == 16:
                Status = "Burned"
            elif int(lst7[1]) == 32:
                Status = "Frozen"
            elif int(lst7[1]) == 64:
                Status = "Paralyzed"
            elif int(lst7[1]) == 128:
                Status = "Toxic"
            pokemon = [name, HP, Max_HP, Level, Status]
            team.append(pokemon)
        if counter == 2:
            counter = -1
        counter += 1
    return team


def make_plot(maxHP,current,output):
    plt.clf()
    y = current/maxHP
    #plt.barh(x, maxHP, color='#607D8B') #green
    if y > 0.5:
        plt.barh(x, current, color='#4CAF50', height = 50/96) #green
    elif y > 0.25 and y <=0.5:
        plt.barh(x, current, color='#FFC107', height = 50/96) #yellow
    else:
        plt.barh(x, current, color='#F44336', height = 50/96) #red
    plt.barh(x, maxHP-current,left = current, color='#212121', height = 50/96) #background
    plt.axis('off')
    plt.savefig(output,bbox_inches='tight', pad_inches = 0, transparent=True, dpi = 96)


def main():
    saved_state = ''
    while True:
        team_file = open(TEAM_PATH)
        fresh_state = fetch_raw_team(team_file)
        if not fresh_state or saved_state == fresh_state:
            continue
        saved_state = fresh_state
        team = parse_team(saved_state)
        try:
            for i in range(0, 6):
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[i][0]) + ".png",
                                "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party" + str(i + 1) + ".png")
                with open("HP" + str(i + 1) + ".txt", "w") as text_file:
                    text_file.write("Lvl: " + str(team[i][3]))
                    text_file.write("\n")
                    text_file.write("HP: " + str(team[i][1]) + "/" + str(team[i][2]))
                    text_file.write("\n")
                    text_file.write("Status: " + str(team[i][4]))
                if team[i][2] == "A":
                    shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png",
                                    "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health" + str(i + 1) + ".png")
                else:
                    make_plot(team[i][2], team[i][1], "health" + str(i + 1) + ".png")
        except Exception:
            pass
        finally:
            time.sleep(1)

main()
