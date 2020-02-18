import sys
from PyQt5 import QtWidgets, QtGui                      # include <QtWidgets> to add Window,button.etc.

def window():

    app = QtWidgets.QApplication(sys.argv)              # The object <app> must be created from class of <QApplication>.

    window = QtWidgets.QWidget()                        # Create an object as <window>.
    window.setWindowTitle("Title :)")

    label = QtWidgets.QLabel(window)
    label.setText("This is NASA!")
    label.move(300, 40)

    label2 = QtWidgets.QLabel(window)
    label2.setPixmap(QtGui.QPixmap("nasa.jpg"))
    label2.move(100, 80)

    window.setGeometry(200, 200, 800, 800)              # 100 coordinates says starts from left upper corner and 500
                                                        # is a lenght of window.
    window.show()

    sys.exit(app.exec_())                               # Thanks to this command the window would be still open.

window()
