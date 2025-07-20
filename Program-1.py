class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

a_input = input("Enter value of a: ")
if '.' in a_input:
    a = float(a_input)
else:
    a = int(a_input)
print("Data type of a:", type(a))

b_input = input("Enter value of b: ")
if '.' in b_input:
    b = float(b_input)
else:
    b = int(b_input)
print("Data type of b:", type(b))
operation = input("Enter type of operation (add, sub, mul, div): ")
print("Data type of operation:", type(operation))

calc = Calculator()

if operation == "add":
    print("Result:", calc.add(a, b))
elif operation == "sub":
    print("Result:", calc.sub(a, b))
elif operation == "mul":
    print("Result:", calc.mul(a, b))
elif operation == "div":
    if b != 0:
        print("Result:", calc.div(a, b))
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation.")
