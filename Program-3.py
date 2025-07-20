a = int(input("Enter an integer value for a: "))
i = 0
count = 0
result = []

while count < a:
    num = 2 * i + 1
    result.append(num)
    count += 1
    i += 1
rem = a % 2
j = 0
temp = []

while j < len(result) - (1 - rem):
    temp.append(result[j])
    j += 1

print("Output:")
k = 0
while k < len(temp):
    print(temp[k], end=", " if k < len(temp) - 1 else "")
    k += 1
