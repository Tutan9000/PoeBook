from PyQt5 import QtCore, QtGui, QtWidgets

from modules.parsing_methods import *
from modules.widget import Widget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent,
                                       flags=QtCore.Qt.Window)
        self.setWindowTitle("PoeBook")
        self.setStyleSheet(
            "QLabel {font-size:10pt;font-family:Verdana;"
            "color:black;font-weight:bold;}")
        self.editor = Widget()
        self.setCentralWidget(self.editor)
        self.path = None
        menuBar = self.menuBar()
        toolBar = QtWidgets.QToolBar()

        myMenuFile = menuBar.addMenu("&Файл")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/new.png"),
                                      "&Новый", self.newFile,
                                      QtCore.Qt.CTRL + QtCore.Qt.Key_N)
        toolBar.addAction(action)
        action.setStatusTip("Создание пустого блокнота")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/open.png"),
                                      "&Открыть", self.onOpenFile,
                                      QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        toolBar.addAction(action)
        action.setStatusTip("Открыть имеющийся файл")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/save.png"),
                                      "&Сохранить", self.fileSave,
                                      QtCore.Qt.CTRL + QtCore.Qt.Key_S)
        toolBar.addAction(action)
        action.setStatusTip("Сохранить")

        action = myMenuFile.addAction("&Сохранить...", self.fileSaveAs)
        action.setStatusTip("Сохранить как...")

        toolBar.addSeparator()
        myMenuFile.addSeparator()

        action = myMenuFile.addAction("&Выход", QtWidgets.qApp.quit,
                                      QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        action.setStatusTip("Завершение работы приложения")

        myMenuEdit = menuBar.addMenu("Правка")

        action = myMenuEdit.addAction("&Рифма", self.rhyme)
        toolBar.addAction(action)
        action.setStatusTip("Найти рифмы для выделенного слова")

        action = myMenuEdit.addAction("&Синоним", self.synonym)
        toolBar.addAction(action)
        action.setStatusTip("Найти синонимы для выделенного слова")

        action = myMenuEdit.addAction("&Эпитет", self.epithets)
        toolBar.addAction(action)
        action.setStatusTip("Найти эпитеты для выделенного слова")

        toolBar.setMovable(True)
        toolBar.setFloatable(False)
        self.addToolBar(toolBar)

        statusBar = self.statusBar()
        statusBar.setSizeGripEnabled(False)
        statusBar.showMessage("Здарова", 5000)

    def rhyme(self):
        papa = self.editor.selectedText()
        if papa != "":
            self.editor.editor2.setText(rhymes(papa))
        else:
            pass

    def synonym(self):
        papa = self.editor.selectedText()
        if papa != "":
            self.editor.editor2.setText(synonym(papa))
        else:
            pass

    def epithets(self):
        papa = self.editor.selectedText()
        if papa != "":
            self.editor.editor2.setText(epithets(papa))
        else:
            pass

    def onOpenFile(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        "Выберите файл", QtCore.QDir.homePath(),
                                                        "(*.txt)")
        if path:
            data = ""
            try:
                with open(path, encoding="utf-8") as f:
                    data = f.read()
            except:
                QtWidgets.QMessageBox.information(self, "Ошибка",
                                                  "Не удалось открыть файл")
            else:
                self.path = path
                self.statusBar().showMessage(f"Файл открыт из {path}", 10000)
                self.editor.editor1.setText(data)

    def newFile(self):
        if self.editor.editor1.toPlainText():
            QtWidgets.QMessageBox.information(self, "Ошибка",
                                              "Не удалось открыть файл")
            self.fileSave()
        self.editor.editor1.setText("")
        self.editor.editor2.setText("")

    def fileSave(self):
        if self.path is None:
            return self.fileSaveAs()
        self._save_to_path(self.path)

    def fileSaveAs(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                        "Выберите файл", QtCore.QDir.homePath(),
                                                        "(*.txt)")
        if not path:
            return
        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.editor1.toPlainText()
        try:
            with open(path, 'w', encoding="utf-8") as f:
                f.write(text)
        except:
            QtWidgets.QMessageBox.information(self, "Блокнот",
                                              "Не удалось сохранить файл")
        else:
            self.path = path
            self.statusBar().showMessage(f"Файл сохранен в {path}", 10000)
