import sympy
from sympy import Expr
from sympy.functions.elementary.trigonometric import cos, sin


def correct_expression(expression: Expr):
    if expression.is_constant():
        return expression, 0

    coef = tr = n = sympy.Number(1)

    if expression.func.is_Mul:
        for arg in expression.args:
            if arg.is_constant():
                coef *= arg
            elif arg.func == sin or arg.func == cos:
                tr *= arg
            else:
                raise Exception("Expression is not in correct form")

    elif expression.func == sin or expression.func == cos:
        tr = expression
    else:
        raise Exception("Expression is not in correct form")

    for arg in tr.args[0].args:
        if arg.is_constant():
            n *= arg

    return coef, n


def is_x(expression: Expr) -> bool:
    for arg in expression.args:
        if len(arg.args) == 0:
            if not arg.is_number and arg != sympy.Symbol('x'):
                return False
        else:
            if not is_x(arg):
                return False
    return True


def is_t(expression: Expr) -> bool:
    for arg in expression.args:
        if len(arg.args) == 0:
            if not arg.is_number and arg != sympy.Symbol('t'):
                return False
        else:
            if not is_t(arg):
                return False
    return True