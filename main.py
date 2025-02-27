# main.py - Arquivo principal
from PyQt5 import QtWidgets
from ui.main_window import AppStore

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = AppStore()
    window.show()
    sys.exit(app.exec_())