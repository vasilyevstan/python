strScore = input("Enter Score: ")

try:
    fScore = float(strScore)
except:
    print("Wrong score")
    quit()

if fScore < 0 or fScore > 1 :
    print("Wrong range")
    quit()

if fScore >= 0.9 :
    print("A")
elif fScore >= 0.8 :
    print("B")
elif fScore >= 0.7 :
    print("C")
elif fScore >= 0.6 :
    print("D")
else :
    print("F")
