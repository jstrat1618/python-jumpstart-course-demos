# Wizard App
Here, we will have a game where a wizard battles several creatures.

##### Note: In this app we do a lot of management of both the game and application. Ideally, in a real application, we should separate those two functions.
 
## Classes
In python classes are defined with the keyword class. 
__Conventionally, classes in python are defined using upper cases! (e.g BeautifulSoup), most other objects are defined using lower case.__

### Magic Methods
Magic methods are methods that apply to a particular class. They are defined inside the class body with the def function with the __ preceeding and succeeding the name of the magic method.
The most import magic method is \_\_init__, which initializes the object being created. The parameter self is required in the \_\_init__ method. This points to the object inside the class.
All methods inside a class take the self parameter.

The \_\_repr__ defines a representation of an object. This method is called by print. So you can define how your objects print.

