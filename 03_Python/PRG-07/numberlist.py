numbers = [6,17,29,55,71]
print("The original list is: " + str(numbers))
for x in range(0, len(numbers)):
    if(x == (len(numbers)-1)):
        print(numbers[x] + numbers[0])
    else:
         print(numbers[x] + numbers[x+1])