largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try :
        number = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None :
        largest = number
    else:
        if number > largest : largest = number

    if smallest is None :
        smallest = number
    else :
        if number < smallest : smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)
