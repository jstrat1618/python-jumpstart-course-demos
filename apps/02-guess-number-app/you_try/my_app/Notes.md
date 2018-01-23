# Guess that Number App
In this game the computer randomly chooses a number betwen 0 and 100. The user is asked to guess the number. The user is told if the number is too high or too low, until the user chooses the correct number.

### Concept: if/ else if /else
One of the fundamental features of a programming language is the ability to make decisions.
The if/ else if/ else is useful to run certain code based on certain conditions.
In python else if is shortended by the command elif.

There are rules to evaluating conditions in Python which we will describe in the next concept as: Truthiness.

### Concept: Truthiness
False # False is false    
[]    # Empty  lists/arrays are false   
{}    # Empty dictionaries are false    
""    # Empty strings are false    
0     # 0 ints are false    
0.0   # 0 floats are false    
None  # None/null/nil pointers are false


**Everything Else is True!**


### Concept: The Shape of a Python Program
Block/suites  are defined with indentation and start with a colon.
Many other programming languages (especially C based languages) use curly braces "{}", but python simply uses tabs.
Avoid manually typing in tabs because a good python editor should do it for you, and you don't want to accidentally place a tab.

#### .format
We can use the .format method on strings to convert objects to string.
The .format method specifies the objects to be converted to a string as the parameters. 
Inside the string simply put curly braces, and inside the specifies the order.

num0 = 0    
num1 = 1   
print("This is {0} and this {1}!".format(num)) #print This is 0 and this is 1!

