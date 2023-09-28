import mpmath
import sympy as sp
import time
import matplotlib.pyplot as plt

def fixed_point_iteration(f, p0, ϵ, max_iterations=100):
    x = sp.symbols('x')
    df = sp.diff(f, x)  # Compute the derivative of f using symbolic tools

    # Convert f and df to mpmath functions for numerical evaluation
    f = sp.lambdify(x, f, 'mpmath')
    df = sp.lambdify(x, df, 'mpmath')

    p = mpmath.mpf(p0)  # Initial guess as a mpmath float
    iterations = 0
    start_time = time.time()
    
    convergence_history = [(p0, 0)]

    while iterations < max_iterations:
        p_new = p - f(p) / df(p)  # Fixed-point iteration formula
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
    f_expr_str = input("Enter the function expression (in terms of x): ")
    initial_guess = float(input("Enter the initial guess: "))
    tolerance = float(input("Enter the tolerance (e.g., 1e-10): "))

    x = sp.symbols('x')
    f_expr = sp.sympify(f_expr_str)

    root, num_iterations, time_taken, convergence_history = fixed_point_iteration(f_expr, initial_guess, tolerance)

    print(f"Estimated Root: {root}")
    print(f"Iterations: {num_iterations}")
    print(f"CPU Time (seconds): {time_taken}")

    
    # Plot the function and convergence history
    x_values, iteration_numbers = zip(*convergence_history)
    
    plt.figure(figsize=(12, 6))

    # Plot the function
    plt.subplot(1, 2, 1)
    x_vals = [mpmath.mpf(val) for val in x_values]
    f_vals = [sp.simplify(x_val) for x_val in x_vals]
    plt.plot(x_vals, f_vals, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function')
    plt.grid(True)
    
    # Plot convergence
    plt.subplot(1, 2, 2)
    plt.plot(iteration_numbers, x_vals, marker='o', linestyle='-')
    plt.xlabel('Iteration Number')
    plt.ylabel('Approximate Root')
    plt.title('Convergence')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
  
