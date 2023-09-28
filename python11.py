import mpmath
import sympy as sp
import time
import matplotlib.pyplot as plt
import numpy as np
import csv
import math


# Input function g(x), initial guess, and tolerance interactively
g_expr_str = input("Enter the function expression g(x) for your fixed-point iteration: ")
f_expr_str = input("Enter the function expression f(x) for which you want to find the root: ")
initial_guess = float(input("Enter the initial guess: "))
tolerance = float(input("Enter the absolute tolerance (e.g., 1e-10): "))

x = sp.symbols('x')
f_expr = sp.sympify(f_expr_str)
g_expr = sp.sympify(g_expr_str)

# Define Python functions for f and g
def f(x_val):
    return f_expr.subs(x, x_val)

def g(x_val):
    return g_expr.subs(x, x_val)

Approximations=[]


def fixed_point_iteration(f, g, p0, ϵ, max_iterations=10):
    x = sp.symbols('x')

    p = mpmath.mpf(p0)
    iterations = 0

    flag = 1
    condition = True
    start_time = time.time()

    while condition:
        p_new = g(p)
        p = p_new
        Approximations.append(p)
        iterations += 1

        if iterations > max_iterations:
            flag = 0
            break

        condition = abs(f(p_new)) > ϵ

        if flag == 1:
            print('\nRequired root is: %0.8f' % p_new)
    else:
        print('\nNot Convergent.')

    end_time = time.time()
    cpu_time = end_time - start_time

    return p, iterations, cpu_time

def plot(xf, xp, x0):
    x = np.linspace(0, 2, 100)
    y = np.vectorize(g_expr)(x)
    plt.plot(x, y)
    plt.plot(xp, np.vectorize(g_expr)(xp), 'bo')
    plt.plot(x0, g_expr(x0), 'ro')
    plt.plot(xf, g_expr(xf), 'go')
    plt.plot(x, x, 'k')
    plt.show()



    root, num_iterations, time_taken = fixed_point_iteration(f, g, initial_guess, tolerance)
    plot(root,Approximations,initial_guess)

    print(f"Estimated Root of f(x): {root}")
    print(f"Iterations: {num_iterations}")
    print(f"CPU Time (seconds): {time_taken}")
