import sympy as sp
import numpy as np
import time
import matplotlib.pyplot as plt

# Define the function f(x)
x = sp.symbols('x')
f = sp.exp(x) + 2 - x + 2*sp.cos(x) - 6

# Define the derivative of f(x)
f_prime = sp.diff(f, x)

# Input: function f, initial guess p0, and tolerance ϵ
p0 = 1.5
epsilon = 1e-20
max_iterations = 1000

# Check if the derivative is zero at the initial guess
if f_prime.subs(x, p0) == 0:
    print("Derivative is zero at the initial guess. Please choose a different initial guess.")
else:
    iterations = []
    root_approximations = []
    function_values = []
    convergence_factors = []

    p = p0
    i = 0
    while i < max_iterations:
        f_val = f.subs(x, p)
        f_prime_val = f_prime.subs(x, p)

        root_approximations.append(p)
        function_values.append(f_val)

        if i > 0:
            convergence_factor = abs(root_approximations[-1] - root_approximations[-2]) / abs(root_approximations[-2] - p)
            convergence_factors.append(convergence_factor)
        else:
            convergence_factors.append(0)

        if abs(f_val) < epsilon:
            break

        p = p - f_val / f_prime_val
        iterations.append(i)

        i += 1

    # Output: Root, number of iterations, and CPU time
    root = root_approximations[-1]
    num_iterations = len(iterations)
    cpu_time = time.process_time()

    print(f"Root found: {root}")
    print(f"Number of iterations: {num_iterations}")
    print(f"CPU time (s): {cpu_time}")

    # Save data to NewtonData.txt
    #data = np.array([iterations, root_approximations, function_values, convergence_factors]).T
    #np.savetxt('NewtonData.txt', data, fmt='%d %.16f %.16f %.16f', header="Iteration Approximation f(Approximation) Convergence Factor")

    # Plot the graph
    x_vals = np.linspace(1, 2, 100)
    f_vals = [f.subs(x, val) for val in x_vals]
    plt.plot(x_vals, f_vals, label='f(x)')
    plt.scatter(root_approximations, function_values, label='Iterations', color='red', marker='x')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton\'s Method')
    plt.legend()
    plt.grid(True)
    plt.show()
