from solution import solve
from ui import UiMainWindow
from enums import EquationType, EquationName

import sympy
from sympy import sqrt
from sympy.simplify.fu import TRpower


class UiCallbackHandler:
    def __init__(self, ui: UiMainWindow):
        self.input = {}
        self.ui: UiMainWindow = ui
        self.ui.calculateButton.clicked.connect(self.on_calculate_clicked)

    def on_calculate_clicked(self):
        self.update_input()

        u = TRpower(sympy.sympify(self.input["u"]))
        u_derivative = TRpower(sympy.sympify(self.input["uDerivative"]))
        heterogeneity = TRpower(sympy.sympify(self.input["heterogeneity"])) if self.input["heterogeneity"] != "" else None

        a = sqrt(sympy.sympify(self.input["a"]))
        l = sympy.sympify(self.input["l"])

        self.ui.log(solve(u, u_derivative, heterogeneity, a, l, self.input["name"], self.input["type"]))

    def update_input(self):
        self.input["u"] = self.ui.uInput.text()
        self.input["uDerivative"] = self.ui.uDerivativeInput.text()
        self.input["a"] = self.ui.aInput.text()
        self.input["l"] = self.ui.lInput.text()
        self.input["heterogeneity"] = self.ui.heterogeneityInput.text()
        self.input["name"] = EquationName.Neumann if self.ui.neumannOptionButton.isChecked() else EquationName.Dirichlet
        self.input["type"] = EquationType.Thermal if self.ui.thermalOptionButton.isChecked() else EquationType.Wave

        self.ui.log("Values updated \n")

        for key, value in self.input.items():
            self.ui.log(f"{key} : {value} \n")



