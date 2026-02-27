temp = int(input("Enter Temperature: "))
hum = int(input("Enter Humidity:" ))
if temp < 18 and 1:
    print("Turn on Heater")
elif 18<temp<25 and hum <60:
    print("Comfortable")
elif 18<temp<25 and hum>60:
    print("Turn on dehumiditien")
elif temp>25 and hum<60:
    print("Turn on AC")
elif temp>25 and hum>60:
    print("Turn on AC and dehumiditien")
