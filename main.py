from models import Theme
from random import choice
import sys

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


if len(sys.argv) == 2 and sys.argv[1] == '2':
    for i in themes:
        print(i)
        ans = input("Continue?")
        if 'no' in ans.lower():
            break

choised_list = themes.copy()

while choised_list:
    theme = choice(choised_list)
    choised_list.remove(theme)

    print(theme)
    ans = input("Continue?")
    if 'no' in ans.lower():
        break
