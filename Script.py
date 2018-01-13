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
    team_file = open(TEAM_PATH)
    saved_state = ''
    while True:
        fresh_state = fetch_raw_team(team_file)
        if not fresh_state or saved_state == fresh_state:
            continue
        saved_state = fresh_state
        team = parse_team(saved_state)
        try:
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[0][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party1.png")
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[1][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party2.png")
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[2][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party3.png")
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[3][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party4.png")
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[4][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party5.png")
            shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\sugimori\\" + str(team[5][0]) + ".png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\team images\\__party6.png")
            time.sleep(1)
            # with open("HP1.txt", "w") as text_file:
            #     text_file.write("Lvl: " + str(100))
            #     text_file.write("\n")
            #     text_file.write("HP: " + str(420) + "/" + str(666))
            #     text_file.write("\n")
            #     text_file.write("Status: " + "High AF")
            with open("HP1.txt", "w") as text_file:
                 text_file.write("Lvl: " + str(team[0][3]))
                 text_file.write("\n")
                 text_file.write("HP: " + str(team[0][1]) + "/" + str(team[0][2]))
                 text_file.write("\n")
                 text_file.write("Status: " + str(team[0][4]))
            with open("HP2.txt", "w") as text_file:
                text_file.write("Lvl: " + str(team[1][3]))
                text_file.write("\n")
                text_file.write("HP: " + str(team[1][1]) + "/" + str(team[1][2]))
                text_file.write("\n")
                text_file.write("Status: " + str(team[1][4]))
            with open("HP3.txt", "w") as text_file:
                text_file.write("Lvl: " + str(team[2][3]))
                text_file.write("\n")
                text_file.write("HP: " + str(team[2][1]) + "/" + str(team[2][2]))
                text_file.write("\n")
                text_file.write("Status: " + str(team[2][4]))
            with open("HP4.txt", "w") as text_file:
                text_file.write("Lvl: " + str(team[3][3]))
                text_file.write("\n")
                text_file.write("HP: " + str(team[3][1]) + "/" + str(team[3][2]))
                text_file.write("\n")
                text_file.write("Status: " + str(team[3][4]))
            with open("HP5.txt", "w") as text_file:
                text_file.write("Lvl: " + str(team[4][3]))
                text_file.write("\n")
                text_file.write("HP: " + str(team[4][1]) + "/" + str(team[4][2]))
                text_file.write("\n")
                text_file.write("Status: " + str(team[4][4]))
            with open("HP6.txt", "w") as text_file:
                text_file.write("Lvl: " + str(team[5][3]))
                text_file.write("\n")
                text_file.write("HP: " + str(team[5][1]) + "/" + str(team[5][2]))
                text_file.write("\n")
                text_file.write("Status: " + str(team[5][4]))
            if team[0][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health1.png")
            # else:
            #     make_plot(666,420,'health1.png')
            else:
                make_plot(team[0][2],team[0][1],'health1.png')
            if team[1][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health2.png")
            else:
                make_plot(team[1][2],team[1][1],'health2.png')
            if team[2][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health3.png")
            else:
                make_plot(team[2][2],team[2][1],'health3.png')
            if team[3][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health4.png")
            else:
                make_plot(team[3][2],team[3][1],'health4.png')
            if team[4][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health5.png")
            else:
                make_plot(team[4][2],team[4][1],'health5.png')
            if team[5][2] =="A":
                shutil.copyfile("C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\Blank.png", "C:\\Users\\Daniel\\Pictures\\Twitch\\NDSRead\\health6.png")
            else:
                make_plot(team[5][2],team[5][1],'health6.png')
        except Exception:
            pass
main()