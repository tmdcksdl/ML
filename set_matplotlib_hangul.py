import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = "c:/Windows/Fonts/malgun.ttf"

if platform.system() == "Darwin":
    print("Hangul OK in your MAC!!!")
    rc("font", family="ArialUnicode MS")
elif platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    print("Hangul OK in Windows!!!")
    rc("font", family=font_name)
else:
    print("Unknown system.. sorry~~~")

plt.rcParams["axes.unicode_minus"] = False
