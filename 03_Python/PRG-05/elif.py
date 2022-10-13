y=1
while y!=100:
    number=int(input("Pick a number: "))
    if number <= 99:
        print("That's a small number buddy")
    elif number >=101:
        print("That's a big number buddy")
    else:
        print("That's the right one")
        y=100