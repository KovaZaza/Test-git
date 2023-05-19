csharp_time = '3:56 6:33 17:39 2:31 10:20 4:03 7:33 1:39 4:46 5:48 5:17 12:43 11:40 8:33 8:40 14:35 5:14 5:46 16:16 5:37 7:21 10:51 7:06 11:51 25:25 14:45 20:50 8:58 '

import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй —
жадный и голодный дракон, который мигом вас съест.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()

    return cave

def new_def():
	...

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()


parse = total_time.split()
lst = list(map(lambda x: x.split(':'), parse))
lst = list(map(lambda x: int(x[0])*60 + int(x[1]), lst))
total_summa = sum(lst)
print(f'total time: {total_summa // 3600}:{total_summa // 60 % 60:02}:{total_summa % 60:02}')
