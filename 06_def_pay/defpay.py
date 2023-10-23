def computepay(h,r):
    if (h % 40) == h:
        pay = h * r
    else:
        pay = 40 * r + (h % 40) * r * 1.5

    return pay

fHours = float(input("Enter Hours: "))
fRate = float(input("Enter rate: "))

p = computepay(fHours,fRate)
print("Pay",p)
