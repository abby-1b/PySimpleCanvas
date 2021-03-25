import pygame
import library.draw as draw

_df = open("library/draw.py", "r").read().split("# Functions")[1].split("\n")
for a in range(len(_df)):
    if _df[a][:10] == "    global":
        _df[a] = ""
    elif "surface == None" in _df[a]: _df[a] = ""
    elif _df[a][:4] == "def ":
        _df[a] = list(_df[a])
        _df[a].insert(_df[a].index("(") + 1, "self, ")
        _df[a] = "".join(_df[a])
    _df[a] = "    " + _df[a]
_df = "\n".join(_df)
_df = _df.replace(", surface=None", "")
_df = _df.replace("\n\n", "\n")
_df = _df.replace("\n    \n", "\n")
_df = _df.replace("surface", "self")
_df = _df.replace("fill_color", "self.fill_color")
_df = _df.replace("translation", "self.translation")
_df = _df.replace("_color_process", "draw._color_process")
_df = "class new_sprite(pygame.Surface):\n    def __init__(self, w, h):\n        super().__init__((w, h), pygame.SRCALPHA, 32)\n        self._fill = super().fill\n        self.translation = [0, 0]\n        self.fill_color = (0, 0, 0)" + _df

print(_df)
exec(_df, locals())
