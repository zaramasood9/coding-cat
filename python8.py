import mpmath
import sympy as sp
import time

def fixed_point_iteration(f, p0, ϵ):
    x = sp.symbols('x')
    df = sp.diff(f, x)  # Compute the derivative of f using symbolic tools

    # Convert f and df to mpmath functions for numerical evaluation
    f = sp.lambdify(x, f, 'mpmath')
    df = sp.lambdify(x, df, 'mpmath')

    p = mpmath.mpf(p0)  # Initial guess as a mpmath float
    iterations = 0
    start_time = time.time()

    while True:
        p_new = p - f(p) / df(p)  # Fixed-point iteration formula
        iterations += 1

        if mpmath.fabs(p_new - p) < ϵ:
            break

        p = p_new

    end_time = time.time()
    cpu_time = end_time - start_time

    return p, iterations, cpu_time

if __name__ == "__main__":
    # Input function, initial guess, and tolerance interactively
    f_expr_str = input("Enter the function expression (in terms of x): ")
    initial_guess = float(input("Enter the initial guess: "))
    tolerance = float(input("Enter the tolerance (e.g., 1e-10): "))

    x = sp.symbols('x')
    f_expr = sp.sympify(f_expr_str)

    root, num_iterations, time_taken = fixed_point_iteration(f_expr, initial_guess, tolerance)

    print(f"Estimated Root: {root}")
    print(f"Iterations: {num_iterations}")
    print(f"CPU Time (seconds): {time_taken}")
