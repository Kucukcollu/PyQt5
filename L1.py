import sys
from PyQt5 import QtWidgets                             # include <QtWidgets> to add Window,button.etc.

def window():

    app = QtWidgets.QApplication(sys.argv)              # The object <app> must be created from class of <QApplication>.

    window = QtWidgets.QWidget()                        # Create an object as <window>.
    window.setWindowTitle("This is a command!")

    window.show()

    sys.exit(app.exec_())                               # Thanks to this command the window would be still open.

window()
