import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()                              # Copy the properties of the class thanks to super func.

        self.init_ui()                                  # Just define for now.

    def init_ui(self):

        self.word_area = QtWidgets.QLabel("Not pushed yet.")
        self.button = QtWidgets.QPushButton("PUSH ME")
        self.count = 0

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.word_area)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.button.clicked.connect(self.click)
        self.show()

    def click(self):

        self.count += 1
        self.word_area.setText("The button pushed " + str(self.count) + " times.")

app = QtWidgets.QApplication(sys.argv)

w = Window()

sys.exit(app.exec_())
