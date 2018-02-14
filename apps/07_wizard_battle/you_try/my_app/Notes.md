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

## Concept: Inheritance
Inheritance is a core concept of OO programming. Inheritance works by first declaring a base type., and then you create other classes that have all the features of a the base type.

In python when we create a class we can supply another class inside parentheses after the class name. This tells python that our class will inherit from the class we supplied in paraentheses.

In our case, we define a Dragon class that inherits from the Creature class. 

#### super method
The super method allows you to call methods from the base type. For example, super.get_roll().

#### Initialization of specialized 
You don't necessarily need to initialize a specialized class at all. You can even just pass the body of the class definition and all the methods and properties of the base type will be inherited. Or you can simply start defining additional methods.

If you want a more specialized initialization, class you call \_\_init __ just as you would in defining the base type and supply the parameters self, along with all of the additional parameters you want including those that are being inherited from the base type. Then you can call super().\_\_init__ and pass the parameters from the base type to the specialized class. You don't necessarily have to include all of them.  This assures those features become part of the specialized class. Then you can  define the additional attributes as we did before.

In python if you want to modify a method in a specialized class you don't need any special keywords (as in other programming languages like override), you just start defining the method with the same name like you did but with the modifications.

## Core Concept: Polymorphism
All specialized classes inherit basic methods from the base type, but the features and methods of a specialized class can be modified/added.

#### Duck Typing
Python has duck typing, which means you don't necessarily have to pass objects of only a particular class to a particular method. As long as the pieces are there for the method, the method will execute. For python's purposes, if it acts like a creature, looks like a creature then it's a creature.
__In statically typed, compiled languages like Java, C++, C#,  you must pass an object of a particular class to a particular method (e.g. you must pass only objects of class creature to the attack method).__ 
Still, class hierarchies are a good idea. It helps reduce code maintenance, it's more understandable and just generally preferred. 


### Simple if/else evaluation
When you only have one test and one assignment you can write the code on one line like     
x = VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE 

     
For example if we want to say y=1 if x>10 and 0 otherwise we could write    
y = 1 if x>10 else 0
