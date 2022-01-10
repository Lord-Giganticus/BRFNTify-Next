import os
from PyQt5 import QtGui, QtWidgets
from BRFNTify import BRFNT
from sys import argv
from pathlib import Path

app = QtWidgets.QApplication([""])

args = argv[1:]

if (Path(args[0]).suffix == ".brfnt"):
    with open(args[0], "rb") as f:
        tmpf = f.read()
        f.close()
    Font = BRFNT(tmpf)
    Font.exportImage().save(f"{os.path.dirname(args[0])}\\{os.path.basename(args[0]).split('.', 1)[0]}.png")
elif (Path(args[0]).suffix == ".png"):
    with open(args[1], "rb") as f:
        tmpf = f.read()
        f.close()
    Font = BRFNT(tmpf)
    image = QtGui.QImage(args[0])
    Font.importImage(image)
    data = Font.save()
    with open(f"{os.path.dirname(args[0])}\\{os.path.basename(args[0]).split('.', 1)[0]}.brfnt", "wb") as f:
        f.write(data)
        f.close()
