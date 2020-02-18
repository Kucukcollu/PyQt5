import sys
from PyQt5 import QtWidgets, QtGui                  # include <QtWidgets> to add Window,button.etc.


def window():
    app = QtWidgets.QApplication(sys.argv)          # The object <app> must be created from class of <QApplication>.

    window = QtWidgets.QWidget()                    # Create an object as <window>.
    window.setWindowTitle("Title :)")

    okay = QtWidgets.QPushButton("OKAY")
    cancel = QtWidgets.QPushButton("CANCEL")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addLayout(h_box)                         # The buttons are at the right lower side corner.

    window.setLayout(v_box)

    window.setGeometry(200, 200, 800, 800)         # 100 coordinates says starts from left upper corner and 500
                                                   # is a lenght of window.

    window.show()

    sys.exit(app.exec_())                          # Thanks to this command the window would be still open.

window()
