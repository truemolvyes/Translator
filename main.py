from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from ui import Ui_Dialog
from translator import translates

lang1 = ['en', 'ru']
lang2 = ['ru', 'en']


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.do_translate)
        self.ui.pushButton_2.clicked.connect(self.swap_lang)

    def swap_lang(self):
        ind1 = lang1.index(lang2[self.ui.comboBox_2.currentIndex()])
        ind2 = lang2.index(lang1[self.ui.comboBox.currentIndex()])
        self.ui.comboBox.setCurrentIndex(ind1)
        self.ui.comboBox_2.setCurrentIndex(ind2)

    def do_translate(self):
        text = self.ui.textEdit.toPlainText()
        fr = lang1[self.ui.comboBox.currentIndex()]
        to = lang2[self.ui.comboBox_2.currentIndex()]

        answer = translates(text, fr, to)
        self.ui.textEdit_2.setText(answer)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
