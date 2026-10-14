import os
import time
from math import sqrt

os.system('')

CSI = '\x1b['
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'

black = f'{CSI}48;5;232m'
red = f'{CSI}48;5;124m'
white = f'{CSI}48;5;255m'
white_block = f'{white}{" " * 1}{RESET}'
print(f'{red}{"  " * 5}{RESET}')
print(f'{red}{"  " * 2}{white}{"  " * 1}{red}{"  " * 2}{RESET}')
print(f'{red}{"  " * 1}{white}{"  " * 3}{red}{"  " * 1}{RESET}')
print(f'{red}{"  " * 2}{white}{"  " * 1}{red}{"  " * 2}{RESET}')
print(f'{red}{"  " * 5}{RESET}')

time.sleep(5)

HOME = f'{CSI}H'


def draw_rings(r):
    for y in range(-8, 9):
        for x in range(-16, 17):
            d1 = sqrt((x + r) ** 2 + y * y)
            d2 = sqrt((x - r) ** 2 + y * y)
            if r - 0.5 <= d1 < r + 0.5 or r - 0.5 <= d2 < r + 0.5:
                print(f'{CSI}40m  ', end='')
            else:
                print(f'{CSI}47m  ', end='')
        print(RESET)


print(f'{CSI}2J', end='')
for i in range(9):
    for r in [2, 4, 6, 8]:
        print(HOME, end='')
        draw_rings(r)
        time.sleep(0.5)

nums_needed = []
nums_others = []
for i in open(r'C:\Users\1\Documents\first_lab\sequence.txt'):
    i = float(i)
    if abs(i) <= 3:
        nums_needed.append(i)
    else:
        nums_others.append(i)
print(f'{ERASE}{RESET}')
g1 = len(nums_needed)
g2 = len(nums_others)
def diagram(g1, g2):
    summ = g1 + g2
    dlina = 50
    print(f'Чисел от -3 до 3 = {g1/summ*100:6.2f}% {CSI}41m{" " * round(dlina*g1/summ)}{RESET}')
    print(f' Остальных чисел = {g2/summ*100:6.2f}% {CSI}42m{" " * round(dlina*g2/summ)}{RESET}')

diagram(g1,g2)
time.sleep(10)