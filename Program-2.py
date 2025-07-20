class OddSeriesGenerator:
    def __init__(self, a):
        self.a = int(a)
    
    def generate_series(self):
        if self.a <= 0:
            return []
        
        odd_numbers = []
        for i in range(self.a):
            odd_number = 2 * i + 1
            odd_numbers.append(odd_number)
        
        return odd_numbers
    
    def print_series(self):
        series = self.generate_series()
        if series:
            series_str = ', '.join(map(str, series))
            print(f"Input a = {self.a}, Output: {series_str}")
        else:
            print(f"Input a = {self.a}, Output: No numbers (a must be positive)")


def generate_odd_series_simple(a):
    return [2*i + 1 for i in range(a)] if a > 0 else []


print("Odd Numbers Series Generator ")
print("This program generates the first 'a' odd numbers")
print()

while True:
    try:
        a = int(input("Enter a positive integer (a): "))
        
        print(f"\n Input Details ")
        print(f"Input a: {a} (Type: {type(a).__name__})")
        
        generator = OddSeriesGenerator(a)
        series = generator.generate_series()
        
        print(f"\n Result ")
        if series:
            series_str = ', '.join(map(str, series))
            print(f"Output: {series_str}")
        else:
            print("Output: No numbers (input must be positive)")
        
        print(f"\n Alternative Method Result ")
        alt_series = generate_odd_series_simple(a)
        if alt_series:
            alt_series_str = ', '.join(map(str, alt_series))
            print(f"Output: {alt_series_str}")
        else:
            print("Output: No numbers")
        
        print()
        
        choice = input("Do you want to generate another series? (y/n): ").lower()
        if choice != 'y' and choice != 'yes':
            print("Thank you for using the series generator!")
            break
            
    except ValueError as e:
        print(f"Error: Please enter a valid integer")
        print()
        
        choice = input("Do you want to try again? (y/n): ").lower()
        if choice != 'y' and choice != 'yes':
            print("Thank you for using the series generator!")
            break
    
    except KeyboardInterrupt:
        print("\nProgram cancelled. Goodbye!")
        break

print("\n Test Cases ")
test_cases = [1, 2, 3, 4, 5, 10]

for test_a in test_cases:
    generator = OddSeriesGenerator(test_a)
    generator.print_series()
