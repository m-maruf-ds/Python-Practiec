mark = int(input("Enter mark: "))

if mark >= 90:
    print("Grade: A, GP: 4.0")
elif mark >= 80:
    print("Grade: B, GP: 3.0")
elif mark >= 70:
    print("Grade: C, GP: 2.0")
elif mark >= 60:
    print("Grade: D, GP: 1.0")
else:
    print("Grade: F, GP: 0.0")