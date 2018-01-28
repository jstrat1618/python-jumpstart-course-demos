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
 
## File IO 
You can open a file with the keyword "open" the first argument is the filename, the second should be either "w" for write, "r" for read or "a" for append. The default is "r" for read.      
Make sure you use the close method after opening a file. For example:   
my_file = open("my_file.txt", "w")   
my_file.close()

Alternatively, you can use  the with method, and when you leave the indented block of code it will automatically call the close method.

with open("my_file.txt", "w") as fout:    
     #commands


 
### The os module
The os module allows you to manage file input and output on all the major platforms.
