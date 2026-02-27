x = int(input())
y = int(input())

#print(f"Before Swap: x = {x}, y = {y}")
print("before swap x,y = ",x,y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After Swap: x = {x}, y = {y}")
print("before swap x,y = ",x,y)
