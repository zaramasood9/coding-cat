import mpmath
import sympy as sp
import time
import matplotlib.pyplot as plt
import numpy as np

def fixed_point_iteration(f, p0, ϵ, max_iterations=100):
    x = sp.symbols('x')
    df = sp.diff(f, x)  # Compute the derivative of f using symbolic tools

    # Convert f and df to mpmath functions for numerical evaluation
    f = sp.lambdify(x, f, 'mpmath')
    df = sp.lambdify(x, df, 'mpmath')

    p = mpmath.mpf(p0)  # Initial guess as an mpmath float
    iterations = 0
    start_time = time.time()
    
    convergence_history = [(p0, 0)]

    while iterations < max_iterations:
        p_new = f(p)  # Fixed-point iteration formula
        iterations += 1
        convergence_history.append((float(p_new), iterations))

        if mpmath.fabs(p_new - p) < ϵ:
            break

        p = p_new

    end_time = time.time()
    cpu_time = end_time - start_time

    return p, iterations, cpu_time, convergence_history

if __name__ == "__main__":
    # Input function, initial guess, and tolerance interactively
    f_expr_str = input("Enter the function expression g(x) for your function (calculate by yourself: ")
    initial_guess = float(input("Enter the initial guess: "))
    tolerance = float(input("Enter the tolerance (e.g., 1e-10): "))

    x = sp.symbols('x')
    f_expr = sp.sympify(f_expr_str)

    # Define a Python function for f
    f = sp.lambdify(x, f_expr, 'numpy')

    root, num_iterations, time_taken, convergence_history = fixed_point_iteration(f_expr, initial_guess, tolerance)

    print(f"Estimated Root: {root}")
    print(f"Iterations: {num_iterations}")
    print(f"CPU Time (seconds): {time_taken}")

    # Generate x values for plotting
    x_vals = np.linspace(float(root) - 2, float(root) + 2, 400)
    f_vals = [f(x_val) for x_val in x_vals]

    # Plot the function and convergence history
    plt.figure(figsize=(12, 6))

    # Plot the function
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, f_vals, label='f(x)')
    plt.plot(x_vals, x_vals, linestyle='--', label='y=x')  # Plot the line y=x
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and y=x')
    plt.legend()
    plt.grid(True)

    # Plot convergence
    plt.subplot(1, 2, 2)
    x_values, iteration_numbers = zip(*convergence_history)
    plt.plot(iteration_numbers, x_values, marker='o', linestyle='-')
    plt.xlabel('Iteration Number')
    plt.ylabel('Approximate Root')
    plt.title('Convergence')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
