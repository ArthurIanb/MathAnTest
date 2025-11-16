from models import Theme
from random import choice, shuffle
import sys


MODES = [1, 2]
with open('test.txt') as f:

    data = f.read().split('&')
    themes = []
    for i in data:
        theme = Theme()
        for line in i.split('\n'):
            stripped = line.strip()
            if len(stripped) == '':
                break
            if stripped and stripped[0] > '0' and stripped[0] <= '9':
                theme.add_subtheme(stripped)
            else:
                theme.set_theme(theme.maintheme + '\n' + stripped[:len(stripped)-1])
        themes.append(theme)


def play(themes: list[Theme]):
    work_theme = themes.copy()
    while work_theme:
        i = work_theme[0]
        print(i)
        work_theme.pop(0)
        if('no' in input("Continue")):
            return 0

def parse_args(args: list[str]):
    start, end = 0, len(themes)
    count = 0
    if len(args) == 0:
        return 1
    mode = int(args[0])

    if len(args) == 1:
        end = len(themes)
        count = end - start
    if len(args) == 2:
        count = int(args[1])
    if len(args) == 3:
        start = int(args[1])
        end = int(args[2])
    if len(args) == 4:
        start = int(args[1])
        end = int(args[2])
        count = int(args[3])
    return mode, start, end, count


def check_args(mode, start, end, count):
    if mode not in [1, 2, 3]:
        return False
    if start < 0 or end > len(themes):
        return False
    if count > len(themes):
        return False
    return True

def main():
    mode, start, end, count = parse_args(sys.argv[1:])
    if not check_args(mode, start, end, count):
        return 0
    choised_list = themes.copy()[start-1:end]
    if mode == 1:
        return play(choised_list)
    if mode == 2:
        shuffle(choised_list)
        return play(choised_list)
    if mode == 3:
        shuffle(choised_list)
        return play(choised_list[:count])
    return "Unreachable"

if __name__ == "__main__":
    main()

