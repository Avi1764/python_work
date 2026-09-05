units = int(input("electricity: "))
senior_citizen = input().strip()
senior_citizen = True if senior_citizen == "True" else False
if units<=100:
    print(1.5*units)
elif units<=200:
    print(2.5*units)
elif units<=500:
    print(4*units)
else:
    print(6*units)
if senior_citizen:
    units -= units*0.10
if senior_citizen:
    units += units*0.5
    print(int(units))


            