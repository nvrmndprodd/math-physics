from PyQt5.QtWidgets import QMessageBox
from enums import EquationName, EquationType

import thermal_conductivity as thermal


def solve(u, u_derivative, heterogeneity, a, l, name, type, logger):
    try:
        if name is EquationName.Neumann and type is EquationType.Thermal:
            return f"answer: {thermal.solve_neumann(u, heterogeneity, a, logger)}"

        elif name is EquationName.Neumann and type is EquationType.Wave:
            pass

        elif name is EquationName.Dirichlet and type is EquationType.Thermal:
            return f"answer: {thermal.solve_dirichlet(u, heterogeneity, a, logger)}"

        elif name is EquationName.Dirichlet and type is EquationType.Wave:
            pass

    except Exception as e:
        exception_window = QMessageBox()
        exception_window.setWindowTitle("Ошибка")
        exception_window.setText(e.__str__())
        exception_window.setIcon(QMessageBox.Critical)
        exception_window.setStandardButtons(QMessageBox.Ok)

        exception_window.exec_()


