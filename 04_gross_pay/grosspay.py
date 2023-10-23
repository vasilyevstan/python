fHours = float(input("Enter Hours: "))
fRate = float(input("Enter rate: "))

if (fHours % 40) == fHours:
    print(fHours * fRate)
else:
    print(40 * fRate + (fHours % 40) * fRate * 1.5)
