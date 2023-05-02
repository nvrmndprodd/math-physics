import verification
from ui import UiMainWindow
from heterogeneity import find_partial_solution

import sympy
from sympy.core.expr import Expr


def solve_dirichlet(expression: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    het = sympy.Number(0) \
        if heterogeneity is None \
        else find_partial_solution(heterogeneity, a)

    expression += het.subs(t, 0)

    if expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos or expression.is_constant():
        expression = sympy.Add(0, expression, evaluate=False)
    elif not expression.func.is_Add:
        raise Exception('Wrong input')

    answer = sympy.Number(0)
    i: int = 0

    logger.log(f"expression: {expression}")
    for component in expression.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.exp(-a ** 2 * n ** 2 * t) * sympy.sin(n * x)

        i += 1

        logger.log(f"c{i} * {sympy.exp(-a ** 2 * n ** 2 * t) * sympy.sin(n * x)}, c{i} = {coef}")

    return answer + het


def solve_neumann(expression: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    het = sympy.Number(0) \
        if heterogeneity is None \
        else find_partial_solution(heterogeneity, a)

    expression += het.subs(t, 0)

    if expression.func.is_Mul or expression.func == sympy.sin or expression.func == sympy.cos or expression.is_constant():
        expression = sympy.Add(0, expression, evaluate=False)
    elif not expression.func.is_Add:
        raise Exception('Wrong input')

    answer = sympy.Number(0)
    i: int = 0

    logger.log(f"expression: {expression}")
    for component in expression.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.exp(-a ** 2 * n ** 2 * t) * sympy.cos(n * x)

        i += 1

        logger.log(f"c{i} * {sympy.exp(-a ** 2 * n ** 2 * t) * sympy.cos(n * x)}, c{i} = {coef}")

    return answer + het
