def count_multiples(numbers):
    result = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result
user_input = input("Enter a list of numbers: ")

try:
    numbers = eval(user_input)  
    if isinstance(numbers, list) and all(isinstance(x, int) for x in numbers):
        output = count_multiples(numbers)
        print("Output:")
        print(output)
    else:
        print("Invalid list. Please enter a list of integers.")
except Exception:
    print("Invalid input format")
