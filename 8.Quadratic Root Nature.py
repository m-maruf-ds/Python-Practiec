a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b*b - 4*a*c

if D > 0:
    print("Real and Distinct roots")
elif D == 0:
    print("Real and Equal roots")
else:
    print("Complex roots")