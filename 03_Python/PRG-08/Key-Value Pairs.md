# Key-Value Pairs
A pairing of a key, a constant that defines the data set and a value, a variable that beloings to this set (e.g. color(key)=red(value)).
## Key terminology
- **Key-Value Pair**  
A pair of related data elements, consisting of a key that defines the data set and a value that belongs to this data set. There are both standard and serialized pairs. A standard pair is formatted in individual pairs, while serialized formatting puts all values belonging to one key into a single set. 
- **Key**  
 A unique identifier in the key-value pair.
- **Value Delimiter**  
Separates individual key-value pairs. When stating multiple key-value pairs, both using standard or serialized format, the ampersand symbol `&` is used. 
- **Key-Value Seperator**  
 Separates a key from the values within a key-value pair. In order to do this the equal symbol `=` is used. 
- **Serial Seperator**  
Seperates individual values within serialized key-value pairs. The string of values is interspersed by a semicolon `;` to indicate the different values.  
- **Dictionary**  
Dictionaries are used to store value in key-value pairs. A distionary is a collection which is ordered, changeable and do not allow duplicates. They are written with curly brackets `{}` and have keys and values.

## Exercise
### Sources
- https://experienceleague.adobe.com/docs/audience-manager/user-guide/reference/key-value-pairs-explained.html?lang=en  
- https://realpython.com/iterate-through-dictionary-python/  
- https://www.w3schools.com/python/python_dictionaries.asp  
- https://stackoverflow.com/questions/26660654/how-do-i-print-the-key-value-pairs-of-a-dictionary-in-python  
- https://www.pythonforbeginners.com/basics/append-dictionary-to-csv-file-in-python  
- https://bobbyhadz.com/blog/python-add-user-input-to-dictionary  
- https://stackoverflow.com/questions/8685809/writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value  
- https://stackoverflow.com/questions/55980027/building-a-csv-based-on-user-input  

### Overcome challenges
Needed to add `'r+'` in order to make the csv file writeable.

### Results
- Created a dictionary, looped over it and printed every key-value pair in the terminal.
- Created a script which asked user for input. Stored this in a dictionary and wrote the information to a csv file 'exercise_8.csv'.