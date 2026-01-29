att=float(input("attendance in %:"))
fees=int(input("fees payment input= 1, not patment=0: "))
assi=int(input("assignment submitted=1, not submitted=0: "))

if fees==0 :
    print("fees not payment")
if att<75 :
    print("attendance less than 75%")
if assi==0 :
    print("assi not submitted")
else:
    print("Eligible for Exam")

