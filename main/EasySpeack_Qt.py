import sys
from PyQt4 import QtGui

from PyQt4.QtGui import QFileDialog

from Speaker import speack, speack_from_file, speack_from_pdf


class MainWindow(QtGui.QMainWindow):
    def click_check_box(self):
        if (self.checkBox.isChecked()):
            self.buttonSpeak.setEnabled(False)
            self.textEdit.setDisabled(True)

            self.buttonSpeakFromFile.setEnabled(True)
            self.buttonSelectTxt.setEnabled(True)
            self.fileNameTextEdit.setDisabled(False)

        else:
            self.buttonSpeak.setEnabled(True)
            self.textEdit.setDisabled(False)

            self.buttonSpeakFromFile.setEnabled(False)
            self.buttonSelectTxt.setEnabled(False)
            self.fileNameTextEdit.setDisabled(True)


    def click_speack(self):
        if self.radio1.isChecked():
            voice = 0
        else:
            voice = 1
        string = self.textEdit.toPlainText().toUtf8().data()
        speack(string, voice)

    def click_speack_from_file(self):
        if(not(self.fileNameTextEdit.toPlainText().isEmpty())):
            if self.radio1.isChecked():
                voice = 0
            else:
                voice = 1
            string = self.fileNameTextEdit.toPlainText().toUtf8().data()
            if string.endswith('.pdf'):
                self.textEdit.setPlainText('PDF')
                speack_from_pdf(string, voice, lambda m: self.textEdit.setPlainText(self.textEdit.toPlainText().toUtf8().data() + '\n' + m))
            else:
                speack_from_file(string, voice)    
    
    def click_select_txt(self):
        self.fileNameTextEdit.setText(QFileDialog.getOpenFileName())

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
        self.checkBox = QtGui.QCheckBox("Speach From File", cWidget)
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.click_check_box)
        self.buttonSpeak = QtGui.QPushButton("Speak")
        self.buttonSpeak.clicked.connect(self.click_speack)
        self.buttonSpeakFromFile = QtGui.QPushButton("Speak From File")
        self.buttonSpeakFromFile.clicked.connect(self.click_speack_from_file)
        vBoxSpeach.addWidget(self.checkBox)
        vBoxSpeach.addWidget(self.buttonSpeak)
        vBoxSpeach.addWidget(self.buttonSpeakFromFile)

        vBoxSelectTxt = QtGui.QVBoxLayout()
        self.buttonSelectTxt = QtGui.QPushButton("Select txt/pdf file")
        self.buttonSelectTxt.clicked.connect(self.click_select_txt)
        vBoxSelectTxt.addWidget(self.buttonSelectTxt)

        self.fileNameTextEdit = QtGui.QTextEdit(cWidget)
        self.fileNameTextEdit.setMaximumHeight(30)

        self.textEdit = QtGui.QTextEdit(cWidget)

        grid.addLayout(vBoxSelectSpeachType, 1, 0)
        grid.addLayout(vBoxSpeach, 1, 1)

        grid.addLayout(vBoxSelectTxt, 2, 1)
        grid.addWidget(self.fileNameTextEdit, 2, 0)

        grid.addWidget(self.textEdit, 3, 0, 1, 2)

        cWidget.setLayout(grid)
        self.setCentralWidget(cWidget)

        #state
        self.buttonSpeak.setEnabled(True)
        self.textEdit.setDisabled(False)

        self.buttonSpeakFromFile.setEnabled(False)
        self.buttonSelectTxt.setEnabled(False)
        self.fileNameTextEdit.setDisabled(True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
