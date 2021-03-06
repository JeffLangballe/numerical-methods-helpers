"""
Numerical Methods techniques
"""

import math


# Gets apprpoximate relative error using new and old x values
def get_relative_error_percent(x_old, x_new):
    return abs((x_new - x_old) / x_new) * 100

# Performs bisection method for n iterations
# Assumes initial guesses bracket a root
# Returns list of tuples of the form
# (iteration, x_lo, x_mid, x_hi, f(x_mid), approximate_relative_error)
def bisection(f, x_lo, x_hi, iterations):
    results = []
    x_mid_old = float('inf')
    for i in range(iterations):
        x_mid = (x_lo + x_hi) / 2
        error = get_relative_error_percent(x_mid_old, x_mid)
        results.append((i + 1, x_lo, x_mid, x_hi, f(x_mid), error))

        test_val = f(x_mid) * f(x_lo)
        if test_val < 0:
            # Root in lower interval
            x_hi = x_mid
        elif test_val > 0:
            # Root in upper interval
            x_lo = x_mid
        else:
            # Found a root exactly!
            break
        x_mid_old = x_mid
    return results

def cubic(x):
    return x*x*x

# Performs netwon-raphson method for n iterations
# Returns list of tuples of the form
# (iteration, root_approx, f(root_approx), approximate_relative_error)
def newton_raphson(f, f_derivative, x_guess, iterations):
    results = []
    x_guess_old = float('inf')
    for i in range(iterations):
        # Get error and append to results list
        error = get_relative_error_percent(x_guess_old, x_guess)
        results.append((i + 1, x_guess, f(x_guess), error))

        # Set variables for next iteration
        x_guess_old = x_guess
        x_guess -= f(x_guess) / f_derivative(x_guess)
    return results


if __name__ == '__main__':
    print(bisection(cubic, -1, 10, 10))
