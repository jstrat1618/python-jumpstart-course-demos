# Journal App
This is a daily journal. It will tell the use how many journal entries are present in the journal, then ask the user if they want to provide additional entries


### Lists
Lists are iterable data structures. You can define an empty list with brackets "[]" and or the keyword "list".
Remember python is a 0-th iterable language so the first element of a list is indexed by 0, the second is indexed by 1.

### for-in loops
The syntax of a for in loop is similar. Start with the keyword "for", a dummy variable to iterate through the iterable data structure the keyword "in"  followed by the iterable data structure.


### reverse function
You can use the reverse function to reverse iterable data structures. For example if we wanted to print out the entries in a list called my_list in reverse order, we could call a for in loop and iterate through reverse(my_list).

### tuples
tuples are non-iterable data structures. You can define a tuple with parentheses. For example:   
"my_tuple = (1,2)" defines a two dimensional tuple "my_tuple" whose first and second elements are 1 and 2 respectively. You can unpack a tuple easily by using a ",". For example,    
x,y = my_tuple defines x as 1 and y as 2

### enumerate function
The enumerate function splits out the an iterable object into tuples 2 dimensional tuples, the first element of which is the index and the second element of which is the content.
 
## Core Concept: File IO 
"open" creates a file stream that requires closing; "with" adds a closing safety.
You can open a file with the keyword "open" the first argument is the filename, the second should be either "w" for write, "r" for read or "a" for append. The default is "r" for read.      
Make sure you use the close method after opening a file. For example:   
my_file = open("my_file.txt", "w")   
my_file.close()

Alternatively, you can use  the with method, and when you leave the indented block of code it will automatically call the close method.

with open("my_file.txt", "w") as fout:    
     #commands


### The os module
The os module allows you to manage file input and output on all the major platforms.

## Core Concept: Complex Conditionals
In python most the keywords "not", "and", "or" operate just as in the vernacular. You can also use & for "and" and | for "or".
Remember Python "Truthiness" ("None", "False", "", {}, [], 0, 0.0 are all False - see the guess the number game app ).
You can also use the common comparison operators (<, <=, >=, ==, !=). You CANNOT use the ! like a solo operator, like the keyword. For example, you can say "not 2==3", but you cannot say "!(2==3)". 

## Core Concept: Doc Strings
When you define a function you can enter a string literal using the ''' operator or the """ operator for a multiline string literal that will provide documentation for your functions. 

##### Pycharm Note
As you'll see pycharm will actually add some of the supporting documentation. 
##### Pycharm Note
You can use Ctrl+Q to look up documentation of a function.


## Core Concept: \_\_name__
Suppose we want to call program.print_header() by importing program. If we had called main() at the bottom it would call the main at the bottom. 
We can avoid this by using the \_\_name__ . \_\_name__  identifies the script being run. 
The \_\_file__ identifies the file being run. When we are running a script \_\_name== is set to \_\_main__, but imported scripts have \_\_name__ and \_\_file__ set to the file name and path respectively. You can uncomment the last two comments in program.py and run program2.py to see this more explicitly. 
main()

at the bottom of program.py, python will only call the main method when program.py is being run. This allows other functions from our code to be imported and used again without calling all the other code without calling the main method.

##### Note:
\_\_name__ and \_\_file__ are sometimes referred to as "dunder name" and "dunder file"


