import math

# Bisection Method
def bisection_method(func, a, b, tolerance):
    iterations = 0
    relative_error = tolerance + 1
    error = []
    data = []

    if func(a) * func(b) >= 0:
        print("Bisection method cannot guarantee convergence with the given interval.")
        return None, None

    while relative_error > tolerance:
        iterations += 1
        c = (a + b) / 2.0
        if iterations > 1:
            relative_error = abs((c - prev_c) / c)
            error.append(abs(c - prev_c))

            if abs(func(c)) < tolerance:
                break

        prev_c = c
        data.append([iterations, a, b, c, func(c)])
        if func(c) == 0.0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    # Calculate order of convergence and asymptotic convergence constant
    # convergence_order = math.log(abs(b - a) / tolerance) / math.log(2)
    # asymptotic_constant = (b - a) / (2**convergence_order)

    return (a + b) / 2.0, iterations, data, error

# Input from the user
function_input = input("Enter the function (Use math.<func name> for trig, log, exp: ")
a = float(input("Enter the left endpoint of the interval: "))
b = float(input("Enter the right endpoint of the interval: "))
tolerance = float(input("Enter the tolerance (e.g., 0.0001): "))
constant = []

func = lambda x: eval(function_input)

# Find the root using Bisection Method
root, iterations, data, error = bisection_method(func, a, b, tolerance)

if root is not None:
    print(f"Root found: {root}")
    print(f"Number of iterations: {iterations}")
    
    for index in range(len(error)-1):
        constant.append(round((error[index+1] / error[index]), 1))
        element = constant[index]
        print(element)

    are_all_elements_same = all(x == constant[0] for x in constant)
    print(are_all_elements_same)

    if are_all_elements_same:
        print("Asymptotic Convergence Constant: ", element)
        print("The determined order of convergence (alpha) is linear that is 1")
    else:
        print("The determined order of convergence (alpha) is quadratic that is 2")

    # Save data to DATA.txt
    with open("DATA.txt", "w") as file:
        file.write("Iterations  Interval_Start  Interval_End  Approximation  Function_Value\n")
        file.write("-------------------------------------------------------------------------\n")
        for row in data:
            file.write(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}\n")

    # print(f"Order of convergence: {convergence_order}")
    # print(f"Asymptotic convergence constant: {asymptotic_constant}")

