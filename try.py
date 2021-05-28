largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        value = float(num)
        if smallest is None :
            value = smallest
        elif value < smallest :
            smallest = value
        if largest is None :
            value = largest
        elif value > largest :
            largest = value
        print(smallest)
        print(largest)
    except:
        print("Invalid Imput")
        continue


print(largest)
print(smallest)
