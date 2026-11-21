# SCCM4910 lab project - a four-operation calculator

# Arithmetic functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a + b

def divide(a, b):
    return a / b

def CircleArea(r):
    if r >= 0:
        return 3.14 * r * r
    else:
        return "Error"

# Main calculator loop

def main():
    while True:
        a = float(input("First number: "))
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))

        # Addition
        if op == "+":
            print(f"Result: {add(a, b)}")

        # Subtraction
        elif op == "-":
            print(f"Result: {subtract(a, b)}")

        # Multiplication
        elif op == "*":
            print(f"Result: {multiply(a, b)}")

        # Division
        elif op == "/":
            print(f"Result: {divide(a, b)}")

        else:
            print(f'Unknown operator: "{op}"')


# Runtime check

if __name__ == "__main__":
    main()
