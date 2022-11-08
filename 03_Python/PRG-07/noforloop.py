numbers = [6,17,29,55,71]
print("The original list is: " + str(numbers))
res = [a + b for a, b in zip(numbers, numbers[1:] + [numbers[0]])]
print("The consecutive overlapping summation is: " + str(res))