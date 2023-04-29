from enum import Enum


class EquationName(Enum):
    Neumann = 0,
    Dirichlet = 1


class EquationType(Enum):
    Thermal = 0,
    Wave = 1
