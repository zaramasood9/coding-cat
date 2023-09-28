import sympy as sp
import numpy as np
import time
import matplotlib.pyplot as plt

# Input: function g(x), initial guess p0, and tolerance ϵ
function_str = input("Enter the function g(x): ")
x = sp.symbols('x')
g = sp.sympify(function_str)
p0 = float(input("Enter the initial guess (p0): ")) # the given interval is [1,2]
epsilon = float(input("Enter the tolerance (ε): "))
max_iterations= 1000
iterations = []
root_approximations = []
function_values = []
relative_error=epsilon + 1
p = p0
i = 0
while i<=max_iterations :
    g_val = g.subs(x, p)

    root_approximations.append(p)
    function_values.append(g_val)

    if i > 0:
        relative_error = abs(root_approximations[-1] - root_approximations[-2]) / abs(root_approximations[-1])
        if relative_error <= epsilon:
            break

    p = g_val
    iterations.append(i)
    i += 1

# Output: Root, number of iterations, and CPU time
root = root_approximations[-1]
num_iterations = len(iterations)
cpu_time = time.process_time()

print(f"Root found: {round(root,4)}")
print(f"Number of iterations: {num_iterations}")
print(f"CPU time (s): {cpu_time}")

# Plot the graph
x_vals = np.linspace(p0 - 1, p0 + 1, 100)  # Adjust the range for the plot
g_vals = [g.subs(x, val) for val in x_vals]
plt.plot(x_vals, g_vals, label='g(x)')
plt.scatter(root_approximations, function_values, label='Iterations', color='red', marker='x')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Fixed-Point Iteration Method')
plt.legend()
plt.grid(True)
plt.show()


