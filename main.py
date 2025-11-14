from models import Theme
from random import choice
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

def main():
    
    if len(sys.argv) < 2:
        return 1
    start = 0
    end = len(themes)
    mode = 0
    if sys.argv[1] == 'help':
        print("py main.py [mode] [start] [end]\nmode = \n\t1: Dont shuffle\n\t2: Shuffle\n\nQuestions in [start:end]")
        return 0
    print("py main.py help -- for help")
    if len(sys.argv) == 4:
        try:
            mode = int(sys.argv[1])
            start = int(sys.argv[2])
            end = int(sys.argv[3])
            if end > len(themes):
                raise ImportError
        except ImportError:
            print("End is too big")
            return 1
        except:
            print("Wrong format")
            return 1
    if len(sys.argv) == 2:
        try:
            mode = int(sys.argv[1])
        except:
            print("Wrong mode")
            return 1
    if len(sys.argv) != 2 and (len(sys.argv)) != 4:
        print("Wrong format")
        return 1
    choised_list = themes.copy()[start:end]
    if mode not in MODES:
        print("Wrong mode")
        return 1
    if mode == 1:
        for i in choised_list:
            print(i)
            ans = input("Continue?")
            if 'no' in ans.lower():
                return 0

    while choised_list:
        theme = choice(choised_list)
        choised_list.remove(theme)

        print(theme)
        ans = input("Continue?")
        if 'no' in ans.lower():
            return 0
    print("Wrong mode")
    return 1

if __name__ == "__main__":
    main()

