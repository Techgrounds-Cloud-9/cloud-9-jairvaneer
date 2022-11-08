y=1
while y!=100:
    number=input("Pick a number: ")
    if (int(number) <= 99):
        print(number+" is a small number buddy")
    elif (int(number) >=101):
        print(number+" is a big number buddy")
    else:
        print(number+" is the right number!")
        y=100