import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle('Grid example')

        cWidget = QtGui.QWidget(self)

        grid = QtGui.QGridLayout(cWidget)  # dichiarazione della griglia

        checkBox = QtGui.QCheckBox("Normal checkbox", cWidget)
        checkBox.setChecked(True)

        triCheck = QtGui.QCheckBox("Tristate checkbox", cWidget)
        triCheck.setTristate(True)
        triCheck.setCheckState(QtCore.Qt.PartiallyChecked)

        vBox = QtGui.QVBoxLayout()
        radio1 = QtGui.QRadioButton("Radio button 1", cWidget)
        radio2 = QtGui.QRadioButton("Radio button 2", cWidget)
        radio3 = QtGui.QRadioButton("Radio button 3", cWidget)
        radio1.setChecked(True)
        vBox.addWidget(radio1)
        vBox.addWidget(radio2)
        vBox.addWidget(radio3)

        vBox2 = QtGui.QVBoxLayout()
        toggle = QtGui.QPushButton("Toggle button")
        toggle.setCheckable(True)
        flat = QtGui.QPushButton("Flat button")
        flat.setFlat(True)
        vBox2.addWidget(toggle)
        vBox2.addWidget(flat)

        textEdit = QtGui.QTextEdit(cWidget)

        grid.addWidget(triCheck, 0, 0)
        grid.addWidget(checkBox, 0, 1)
        grid.addLayout(vBox, 1, 0)
        grid.addLayout(vBox2, 1, 1)
        grid.addWidget(textEdit, 2, 0, 1, 2)

        cWidget.setLayout(grid)
        self.setCentralWidget(cWidget)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
