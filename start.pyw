import sys

from PyQt5 import QtGui, QtWidgets

from modules.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(r"images/svd.png"))
window = MainWindow()
window.resize(700, 600)
window.show()
sys.exit(app.exec_())
