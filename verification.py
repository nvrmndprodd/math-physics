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