print("Hello Programmmers!")

ab = float(input("Acc. Balance: "))
wb = float(input("Withdrawl. Balance: "))

if wb%100!=0 :
    print("Invalid Amount")
elif ab<wb :
    print("Insufficient funds")
elif ab-wb< 500 :
    print("Minium balace rule violated")
else :
    print("Transaction Sucessful")