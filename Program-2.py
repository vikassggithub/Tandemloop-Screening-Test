a = int(input("Enter an integer value for a: "))
i = 0
count = 0
while count < a:
    num = 2 * i + 1
    print(num, end="")
    count = count + 1
    i = i + 1
    if count < a:
        print(", ", end="")

