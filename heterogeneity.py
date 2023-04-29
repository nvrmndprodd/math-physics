import sympy
from sympy import Expr
from verification import is_x, is_t


def divide(expression: Expr):
    F = G = sympy.Number(1)

    if is_t(expression):
        return expression, G
    elif is_x(expression):
        return F, expression

    if not expression.func.is_Mul:
        raise Exception('Wrong input')

    for arg in expression.args:
        if is_t(arg):
            F *= arg
        elif is_x(arg):
            G *= arg
        else:
            raise Exception('Wrong input')

    return F, G


def find_partial_solution(expression: Expr, a):
    x, t, k, c1 = sympy.symbols('x t k C1')

    F, G = divide(expression)

    k_squared = sympy.solveset(sympy.Eq(G.diff(x, x), -(k) ** 2 * G), k ** 2).args[0]

    w = sympy.symbols('w', cls=sympy.Function)
    w = sympy.dsolve(sympy.Eq(w(t).diff(t), (a ** 2) * (-1) * k_squared * w(t) + F), w(t)).args[1]

    return w.subs(c1, 0) * G
