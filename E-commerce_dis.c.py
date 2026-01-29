#E-Commerce Discount System

cart=int(input("cart value input: "))
memb_type=input("member type  gold, silver or none: ")
coupon=input("yes or no: ")
dis=0
if memb_type == "silver":
    dis=.1
elif memb_type == "gold":
    dis=.2
else:
    dis=0
if coupon == "yes" and cart > 3000:
    dis=dis+0.05
if dis>0.25:
    dis=0.25
pay_amount= cart-(cart*dis)
print("payable amount (in BDT):",pay_amount)