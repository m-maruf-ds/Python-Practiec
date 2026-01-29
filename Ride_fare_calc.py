bf=50
cpk=10
ph_cost=0
nh_cost=0
fare=0
dis=float(input("Distance in KM: "))
ph=int(input("pich hour status yes for 1 and no for 0: "))
nh=int(input("nigth time yes for 1 and no for 0: "))
if ph==1 :
    ph_cost=1
    fare = bf+(dis*cpk)+(dis*ph_cost*1.5)+(nh_cost*30)
if nh==1 :
    nh_cost=1
    fare = bf+(dis*cpk)+(dis*ph_cost*1.5)+(nh_cost*30)
if dis<2 and fare<80 :
    fare=80

print(round(fare))
