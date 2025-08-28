weight = int(input("Weight : "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.454
    print(f" You are {converted} kilos")
else:
    converted = weight / 0.454
    print(f" You're {converted} pounds")
