import sys
from PyQt4 import QtGui

from Speaker import speack


class MainWindow(QtGui.QMainWindow):
    def click_speack(self):
        if self.radio1.isChecked():
            voice = 0
        else:
            voice = 1
        string = self.textEdit.toPlainText().toUtf8().data()
        speack(string, voice)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle('EasySpeak')

        cWidget = QtGui.QWidget(self)

        grid = QtGui.QGridLayout(cWidget)

        vBoxSelectSpeachType = QtGui.QVBoxLayout()
        self.radio1 = QtGui.QRadioButton("simple_google_tts", cWidget)
        self.radio2 = QtGui.QRadioButton("espeach", cWidget)
        self.radio1.setChecked(True)
        vBoxSelectSpeachType.addWidget(self.radio1)
        vBoxSelectSpeachType.addWidget(self.radio2)

        vBoxSpeach = QtGui.QVBoxLayout()
        buttonSpeak = QtGui.QPushButton("Speak")
        buttonSpeak.clicked.connect(self.click_speack)
        vBoxSpeach.addWidget(buttonSpeak)

        self.textEdit = QtGui.QTextEdit(cWidget)

        grid.addLayout(vBoxSelectSpeachType, 1, 0)
        grid.addLayout(vBoxSpeach, 1, 1)
        grid.addWidget(self.textEdit, 2, 0, 1, 2)

        cWidget.setLayout(grid)
        self.setCentralWidget(cWidget)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
