from PyQt5 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setStyleSheet(
            "QTextEdit#mainEditor {font-size:12pt;font-family:Verdana;"
            "color:black;font:italic}"
            "QTextEdit#addEditor {font-size:10pt;font-family:Verdana;"
            "color:black;background-color: #DFDFDF}")

        self.editor1 = QtWidgets.QTextEdit()
        self.editor1.setObjectName("mainEditor")
        self.editor2 = QtWidgets.QTextEdit()
        self.editor2.setObjectName("addEditor")
        self.BoxMain = QtWidgets.QHBoxLayout()
        self.BoxMain.addWidget(self.editor1)
        self.BoxMain.addWidget(self.editor2)
        self.setLayout(self.BoxMain)

    def selectedText(self):
        return self.editor1.textCursor().selectedText()
