import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()                              # Copy the properties of the class thanks to super func.

        self.init_ui()

    def init_ui(self):

        self.word_area = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("CLEAR")
        self.write = QtWidgets.QPushButton("WRITE")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.word_area)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.write)
        v_box.addStretch()

        self.setLayout(v_box)

        self.clear.clicked.connect(self.click)
        self.write.clicked.connect(self.click)

        self.show()

    def click(self):

        sender = self.sender()

        if sender.text() == "CLEAR":
            self.word_area.clear()

        else:
            print(self.word_area.text())

app = QtWidgets.QApplication(sys.argv)

w = Window()

sys.exit(app.exec_())
