class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()
    
    def calculate(self):
        if self.operation == 'add' or self.operation == '+':
            return self.addition()
        elif self.operation == 'subtract' or self.operation == '-':
            return self.subtraction()
        elif self.operation == 'multiply' or self.operation == '*':
            return self.multiplication()
        elif self.operation == 'divide' or self.operation == '/':
            return self.division()
        else:
            raise ValueError(f"Invalid operation: {self.operation}")
   
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b
    
    def print_details(self):
        print(f"Input a: {self.a} (Type: {type(self.a).__name__})")
        print(f"Input b: {self.b} (Type: {type(self.b).__name__})")
        print(f"Operation: '{self.operation}' (Type: {type(self.operation).__name__})")
print("Dynamic Calculator")
print("Available operations: add, sub, mul, divide (or +, -, *, /)")
print()

while True:
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation: ")

        calc = Calculator(a, b, operation)

        print("\n--- Input Details ---")
        calc.print_details()

        result = calc.calculate()
 
        print(f"\n--- Result ---")
        print(f"Calculation: {a} {operation} {b} = {result}")
        print(f"Result Type: {type(result).__name__}")
        print()
        choice = input("Do you want to perform another calculation? (y/n): ").lower()
        if choice != 'y' and choice != 'yes':
            print("Thank you for using the calculator!")
            break
            
    except ValueError as e:
        print(f"Error: {e}")
        print()
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice != 'y' and choice != 'yes':
            print("Thank you for using the calculator!")
            break
    except KeyboardInterrupt:
        print("\nCalculation cancelled. Goodbye!")
        break
