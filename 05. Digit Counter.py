n = int(input("Enter number: "))

if n == 0:
    count = 1
else:
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        count += 1
        n //= 10

print("Number of digits:", count)