import verification
from ui import UiMainWindow
from heterogeneity import find_partial_solution

import sympy
from sympy.core.expr import Expr


def solve_dirichlet(expression_u: Expr, expression_du: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    het = sympy.Number(0) \
        if heterogeneity is None \
        else find_partial_solution(heterogeneity, a)

    expression_u += het.subs(t, 0)

    if expression_u.func.is_Mul or expression_u.func == sympy.sin or expression_u.func == sympy.cos or expression_u.is_constant():
        expression_u = sympy.Add(0, expression_u, evaluate=False)
    elif not expression_u.func.is_Add:
        raise Exception('Wrong input')

    answer = sympy.Number(0)
    i: int = 0

    logger.log(f"expression: {expression_u}")

    for component in expression_u.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.cos(a * n * t) * sympy.sin(n * x)

        i += 1

        logger.log(f"c{i} * {sympy.cos(a * n * t) * sympy.sin(n * x)}, c{i} = {coef}")

    if expression_du.func.is_Mul or expression_du.func == sympy.sin or expression_du.func == sympy.cos or expression_du.is_constant():
        expression_du = sympy.Add(0, expression_du, evaluate=False)
    elif not expression_du.func.is_Add:
        raise Exception('Wrong input')

    logger.log("")
    logger.log(f"expression: {expression_du}")

    for component in expression_du.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.sin(a * n * t) * sympy.sin(n * x)

        i += 1

        logger.log(f"c{i} * {sympy.sin(a * n * t) * sympy.sin(n * x)}, c{i} = {coef}")

    return answer + het


def solve_neumann(expression_u: Expr, expression_du: Expr, heterogeneity: Expr, a, logger: UiMainWindow):
    x, t = sympy.symbols("x t")

    het = sympy.Number(0) \
        if heterogeneity is None \
        else find_partial_solution(heterogeneity, a)

    expression_u += het.subs(t, 0)

    if expression_u.func.is_Mul or expression_u.func == sympy.sin or expression_u.func == sympy.cos or expression_u.is_constant():
        expression_u = sympy.Add(0, expression_u, evaluate=False)
    elif not expression_u.func.is_Add:
        raise Exception('Wrong input')

    answer = sympy.Number(0)
    i: int = 0

    logger.log(f"expression: {expression_u}")

    for component in expression_u.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        answer += coef * sympy.cos(a * n * t) * sympy.cos(n * x)

        i += 1

        logger.log(f"c{i} * {sympy.cos(a * n * t) * sympy.cos(n * x)}, c{i} = {coef}")

    if expression_du.func.is_Mul or expression_du.func == sympy.sin or expression_du.func == sympy.cos or expression_du.is_constant():
        expression_du = sympy.Add(0, expression_du, evaluate=False)
    elif not expression_du.func.is_Add:
        raise Exception('Wrong input')

    logger.log("")
    logger.log(f"expression: {expression_du}")

    for component in expression_du.args:
        if component.is_zero:
            continue

        coef, n = verification.correct_expression(component)

        if n != 0:
            answer += coef * sympy.sin(a * n * t) * sympy.cos(n * x)
            logger.log(f"c{i} * {sympy.sin(a * n * t) * sympy.cos(n * x)}, c{i} = {coef}")
        else:
            answer += coef * t
            logger.log(f"c{i} * {t}, c{i} = {coef}")

        i += 1

    return answer + het
