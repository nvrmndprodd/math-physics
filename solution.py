from PyQt5.QtWidgets import QMessageBox
from enums import EquationName, EquationType


def solve(u, u_derivative, heterogeneity, a, l, name, type):
    try:
        if name is EquationName.Neyman and type is EquationType.Thermal:
            pass

        elif name is EquationName.Neyman and type is EquationType.Wave:
            pass

        elif name is EquationName.Dirichle and type is EquationType.Thermal:
            pass

        elif name is EquationName.Dirichle and type is EquationType.Wave:
            pass

    except Exception as e:
        exception_window = QMessageBox()
        exception_window.setWindowTitle("Ошибка")
        exception_window.setText(e.__str__())
        exception_window.setIcon(QMessageBox.Critical)
        exception_window.setStandardButtons(QMessageBox.Ok | QMessageBox.Retry)

        x = exception_window.exec_()


