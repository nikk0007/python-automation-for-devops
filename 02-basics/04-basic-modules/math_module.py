import math

# 1. Calculate the square root of a number
def calculate_square_root(number):
    """Returns the square root of the given number using math.sqrt()"""
    return math.sqrt(number)

# 2. Calculate the greatest common divisor (GCD) of two numbers
def calculate_gcd(a, b):
    """Returns the GCD of two numbers using math.gcd()"""
    return math.gcd(a, b)

# 3. Calculate the factorial of a number
def calculate_factorial(n):
    """Returns the factorial of a number using math.factorial()"""
    return math.factorial(n)

# 4. Rounding a number up and down
def round_numbers(number):
    """Returns the ceil and floor of a number using math.ceil() and math.floor()"""
    ceil_value = math.ceil(number)  # Round up
    floor_value = math.floor(number)  # Round down
    return ceil_value, floor_value

# 5. Convert degrees to radians and vice versa
def convert_degrees_radians(degrees):
    """Converts degrees to radians and radians back to degrees using math.radians() and math.degrees()"""
    radians = math.radians(degrees)  # Degrees to radians
    degrees_back = math.degrees(radians)  # Radians to degrees
    return radians, degrees_back

# 6. Calculate the value of pi, e, and logarithms
def calculate_constants_and_logarithms(number):
    """Returns the value of pi, e, and the natural log of a number using math.pi, math.e, and math.log()"""
    pi_value = math.pi
    e_value = math.e
    log_value = math.log(number)  # Natural log
    log_base10_value = math.log10(number)  # Logarithm base 10
    return pi_value, e_value, log_value, log_base10_value

# 7. Trigonometric functions (sin, cos, tan)
def calculate_trigonometric_functions(angle_in_degrees):
    """Returns the sine, cosine, and tangent of an angle using math.sin(), math.cos(), and math.tan()"""
    angle_in_radians = math.radians(angle_in_degrees)  # Convert degrees to radians
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    tangent_value = math.tan(angle_in_radians)
    return sine_value, cosine_value, tangent_value

# Main function to demonstrate the use of the math module methods
if __name__ == "__main__":
    # Example usage of each method

    # 1. Square root
    number = 16
    print(f"Square root of {number}: {calculate_square_root(number)}")

    # 2. GCD of two numbers
    num1, num2 = 48, 180
    print(f"GCD of {num1} and {num2}: {calculate_gcd(num1, num2)}")

    # 3. Factorial
    factorial_num = 5
    print(f"Factorial of {factorial_num}: {calculate_factorial(factorial_num)}")

    # 4. Ceil and floor
    decimal_number = 3.67
    ceil_val, floor_val = round_numbers(decimal_number)
    print(f"Ceiling of {decimal_number}: {ceil_val}, Floor: {floor_val}")

    # 5. Degrees to Radians and vice versa
    degrees = 45
    radians, degrees_back = convert_degrees_radians(degrees)
    print(f"{degrees} degrees in radians: {radians}, and back to degrees: {degrees_back}")

    # 6. Constants and logarithms
    log_number = 10
    pi_val, e_val, log_val, log_base10_val = calculate_constants_and_logarithms(log_number)
    print(f"Pi: {pi_val}, e: {e_val}, log({log_number}): {log_val}, log10({log_number}): {log_base10_val}")

    # 7. Trigonometric functions
    angle = 30
    sine, cosine, tangent = calculate_trigonometric_functions(angle)
    print(f"Sine({angle} degrees): {sine}, Cosine: {cosine}, Tangent: {tangent}")
