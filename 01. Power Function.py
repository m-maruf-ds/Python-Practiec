def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print("Result:", power(b, e))