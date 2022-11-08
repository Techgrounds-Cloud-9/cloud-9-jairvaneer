# Loops
Loops are used to make a line of code run multiple times.
## Key terminology
- **While Loop**  
A 'while loop' is used to make a code run for as long as a previously defined condition is met. If this condition is met every time, this loop wil run forever.
- **For Loop**  
A 'for loop' runs for a previuosly determined number of times.

## Exercise
### Sources
- https://www.w3schools.com/python/python_while_loops.asp  
- https://pythonguides.com/multiply-in-python/#:~:text=In%20python%2C%20to%20multiply%20number,%E2%80%9D%20*%20%E2%80%9D%20to%20multiply%20number.&text=After%20writing%20the%20above%20code,used%20to%20multiply%20the%20number  
- https://www.w3schools.com/python/python_for_loops.asp

### Overcome challenges
It took me a few tries to remember I had to change the input to integer in order for the conditions to be numerical.

### Results
- Used a while loop to print the value of x in every iteration of the loop, with the value of x increasing every time as long as the value of x was smaller or equal to 10.  
- Ran the for loop without assigning value to `i`. The loop still ran because a for loop doesn't require an indexing variable to be set beforehand. If no indexing value is set, it will by default start from 0.
- Used the for loop to print the value of `x` multiplied by the value of `i`, for up to 50 iterations. This means that without specifying the indexing value, and stating `for i in range(50)`, this script will run from 0 until 49, which is 50 iterations.
- Used a for loop to loop over the array, which printed every name individually.