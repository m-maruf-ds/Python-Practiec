a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Valid triangle: Equilateral")
    elif a == b or b == c or a == c:
        print("Valid triangle: Isosceles")
    else:
        print("Valid triangle: Scalene")
else:
    print("Not a valid triangle")