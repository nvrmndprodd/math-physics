from ui import UiMainWindow
from enums import EquationType, EquationName

import sympy
from sympy.simplify.fu import TRpower


class UiCallbackHandler:
    def __init__(self, ui: UiMainWindow):
        self.input = {}
        self.ui: UiMainWindow = ui
        self.ui.calculateButton.clicked.connect(self.on_calculate_clicked)

    def on_calculate_clicked(self):
        self.update_input()

        u = TRpower(sympy.sympify(self.input["u"]))
        uDerivative = TRpower(sympy.sympify(self.input["uDerivative"]))
        heterogeneity = TRpower(sympy.sympify(self.input["heterogeneity"])) if self.input["heterogeneity"] is not "" else None

        a = sympy.sympify(self.input["a"])
        l = sympy.sympify(self.input["l"])

        if self.input["name"] is EquationName.Neyman and self.input["type"] is EquationType.Thermal:
            pass

        elif self.input["name"] is EquationName.Neyman and self.input["type"] is EquationType.Wave:
            pass

        elif self.input["name"] is EquationName.Dirichle and self.input["type"] is EquationType.Thermal:
            pass

        elif self.input["name"] is EquationName.Dirichle and self.input["type"] is EquationType.Wave:
            pass

    def update_input(self):
        self.input["u"] = self.ui.uInput.text()
        self.input["uDerivative"] = self.ui.uDerivativeInput.text()
        self.input["a"] = self.ui.aInput.text()
        self.input["l"] = self.ui.lInput.text()
        self.input["heterogeneity"] = self.ui.heterogeneityInput.text()
        self.input["name"] = EquationName.Neyman if self.ui.neymanOptionButton.isChecked() else EquationName.Dirichle
        self.input["type"] = EquationType.Thermal if self.ui.thermalOptionButton.isChecked() else EquationType.Wave

        print("Values updated")

        for key, value in self.input:
            print(f"{key} : {value}")



