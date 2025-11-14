
class Theme:
    def __init__(self, maintheme: str="", subthemes: list[str]|None=None):
        self.maintheme = maintheme
        if subthemes is None:
            self.subthemes = []
        else:
            self.subthemes = subthemes

    def set_theme(self, theme: str):
        self.maintheme = theme

    def add_subtheme(self, subtheme: str):
        self.subthemes.append(subtheme)

    def set_subthemes(self, subthemes: list[str]):
        self.subthemes = subthemes

    def extend_subthemes(self, subthemes: list[str]):
        self.subthemes.extend(subthemes)

    def __str__(self):
        out = self.maintheme
        for i in self.subthemes:
            out += f"\n{i}"
        return out