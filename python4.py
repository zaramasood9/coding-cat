import math

def bisection_method(func, a, b, tolerance):
    iterations = 0
    relative_error = tolerance + 1  # initial relative error
    error = []

    file = open('DATA.txt', 'w')
    file.write('n          an          bn          pn          f(pn)\n')
    
    if func(a) * func(b) >= 0:
        print("Bisection method is not applicable to this interval. Please provide a new interval.")
        return None

    while relative_error > tolerance:
        c = (a + b) / 2
        mid = c  
        if func(c) == 0:
            return c, iterations
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        
        print('iteration number: ' + str(iterations) + ", P" + str(iterations) + ": " + str(mid) + ", f(P" + str(iterations) + "): " + str(func(mid)))
        file.write(' ' + str(round(iterations, 3)) + '      ' + str(round(a, 3)) + '     ' + str(round(b, 3)) + '     ' + str(round(mid, 3)) + '       ' + str(round(func(mid), 3)) + '\n')

        iterations += 1

        if iterations > 1:
            relative_error = abs((c - prev_c) / c)
            error.append(abs(c - prev_c))

        #if abs(func(c)) < tolerance or b - a < tolerance:
            #break
        prev_c = c

    root = (a + b) / 2
    file.close()  
    return root, iterations, error

try:
    function_input = input("Enter the function (Use math.<func name> for trig, log, exp): ")
    interval_start = eval(input("Enter endpoint 1 of the interval: "))
    interval_end = eval(input("Enter endpoint 2 of the interval: "))
    tolerance = float(input("Enter the tolerance (e.g., 0.0001): "))
    constant = []

    # Define a lambda function to evaluate the user-provided function
    func = lambda x: eval(function_input)

    result = bisection_method(func, interval_start, interval_end, tolerance)

    if result is not None:
        root, iterations, error = result
        print(f"Root: {root}")
        print(f"Number of iterations: {iterations}")

        for index in range(len(error) - 1):
            constant.append(round((error[index + 1] / error[index]), 1))
            element = constant[index]
            print(element)

        are_all_elements_same = all(x == constant[0] for x in constant)
        print(are_all_elements_same)

        if are_all_elements_same:
            print("Asymptotic Convergence Constant: ", element)
            print("The determined order of convergence (alpha) is linear that is 1")
        else:
            print("The determined order of convergence (alpha) is quadratic that is 2")
    else:
        print("Bisection method did not converge to a root within the specified conditions.")

except ValueError:
    print("Invalid input. Please enter valid numerical values for the interval and tolerance.")
except SyntaxError:
    print("Invalid function input. Please provide a valid mathematical function.")
