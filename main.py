from PyQt5 import QtWidgets

from ui_callback_handler import UiCallbackHandler
from ui import UiMainWindow


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = UiMainWindow()
    ui.setup_ui(MainWindow)

    callback_handler = UiCallbackHandler(ui)

    MainWindow.show()
    sys.exit(app.exec_())

