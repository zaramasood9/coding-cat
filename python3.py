import math

def bisection_method(func, a, b, tolerance):
    if func(a) * func(b) >= 0:
        print("Bisection method cannot guarantee convergence on the given interval.")
        return None, None

    iteration = 0
    root = None
    relative_error = tolerance + 1  # Initialize relative error to a value greater than tolerance

    while relative_error > tolerance:
        c = (a + b) / 2
        fa = func(a)
        fb = func(b)
        fc = func(c)

        if fc == 0:
            root = c
            break

        if fa * fc < 0:
            b = c
        else:
            a = c

        iteration += 1

        if iteration > 1:
            relative_error = abs((c - prev_c) / c)
            if abs(fc) < tolerance:
                break

        prev_c = c

    return root, iteration

if __name__ == "__main__":
    # Input: function as a string, interval [a, b], and tolerance
    function_str = 'x - math.cos(x)'
    a = 0
    b = math.pi
    tolerance = 0.0001

    try:
        func = lambda x: eval(function_str)  # Convert the input string to a callable function
        root, iterations = bisection_method(func, a, b, tolerance)

        if root is not None:
            print("Please choose a different interval for Bisection Method.")
        else:
            print(f"Root found: {root}")
            print(f"Number of iterations: {iterations}")
            print("Please choose a different interval for Bisection Method.")
    except SyntaxError:
        print("Invalid function input. Make sure the function is in a valid Python format.")
