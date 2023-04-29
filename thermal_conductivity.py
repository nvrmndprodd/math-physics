import verification

import sympy
from sympy.core.expr import Expr

from ui import UiMainWindow


def solve_dirichlet(expression: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    heterogeneity = sympy.Number(0) if heterogeneity is None else sympy.Number(0)
    heterogeneity.subs(t, 0)

    expression = expression + heterogeneity

    if expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos:
        expression = sympy.Add(0, expression, evaluate=False)
    elif not expression.func.is_Add:
        raise Exception('Failed to solve linear Combination')

    answer = sympy.Number(0)
    i: int = 0

    for component in expression.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.exp(-a**2 * n**2 * t) * sympy.sin(n * x)

        logger.log(f"c{i} * {sympy.exp(-a**2 * n**2 * t) * sympy.sin(n * x)}, c{i} = {coef}")

        i += 1

    return answer - heterogeneity


def solve_neumann(expression: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    heterogeneity = sympy.Number(0) if heterogeneity is None else sympy.Number(0)
    heterogeneity.subs(t, 0)

    expression = expression + heterogeneity

    if expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos:
        expression = sympy.Add(0, expression, evaluate=False)
    elif not expression.func.is_Add:
        raise Exception('Failed to solve linear Combination')

    answer = sympy.Number(0)
    i: int = 0

    for component in expression.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.exp(-a**2 * n**2 * t) * sympy.cos(n * x)

        logger.log(f"c{i} * {sympy.exp(-a**2 * n**2 * t) * sympy.cos(n * x)}, c{i} = {coef}")

        i += 1

    return answer - heterogeneity
