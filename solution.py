from PyQt5.QtWidgets import QMessageBox
from enums import EquationName, EquationType

import thermal_conductivity as thermal
import wave


def solve(u, u_derivative, heterogeneity, a, l, name, type, logger):
    try:
        if name is EquationName.Neumann and type is EquationType.Thermal:
            answer = thermal.solve_neumann(u, heterogeneity, a, logger)
            print(answer)
            return f"answer: {answer}"

        elif name is EquationName.Neumann and type is EquationType.Wave:
            answer = wave.solve_neumann(u, u_derivative, heterogeneity, a, logger)
            print(answer)
            return f"answer: {answer}"

        elif name is EquationName.Dirichlet and type is EquationType.Thermal:
            answer = thermal.solve_dirichlet(u, heterogeneity, a, logger)
            print(answer)
            return f"answer: {answer}"

        elif name is EquationName.Dirichlet and type is EquationType.Wave:
            answer = wave.solve_dirichlet(u, u_derivative, heterogeneity, a, logger)
            print(answer)
            return f"answer: {answer}"

    except Exception as e:
        exception_window = QMessageBox()
        exception_window.setWindowTitle("Ошибка")
        exception_window.setText(e.__str__())
        exception_window.setIcon(QMessageBox.Critical)
        exception_window.setStandardButtons(QMessageBox.Ok)

        exception_window.exec_()


