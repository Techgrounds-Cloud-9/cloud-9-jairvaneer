numbers = [6,17,29,55,71]
print("The original list is: " + str(numbers))
for x in range(len(numbers)):
    if x < 4:
        print (numbers[x] + numbers[x+1])
else:
    print (numbers[0] + numbers [4])