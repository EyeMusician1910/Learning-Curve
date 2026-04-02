# OOPS - Object Oriented Programming System

    -Advantages:
        -Clear structure to the programs
        -Makes codes easier to maintain
        -Helps to keep the code "Don't Repeat Yourself"
        -Allows to make application with reusable and less code.
    
-Classes- Defines what an object should look like,and based on the class,the object is created.

-All classes have an in-built method called  __init__(),executed when the class is being initiated.
-used to assign values to object properties, or to perform operations that are necessary when the object is being created.
-why use __init__?:without it,need to set properties manually for each object.

# self Parameter:
    -is reference to the current instance of the class, and is used to access variables that belongs to the class.
    -It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.
    -Why?-Python would not know which object's properties you want to access
    -Can access the Properties of another function using self.
    -we can also call methods using self.

# Properties:
    -Variables that belong to a class,used to store data in objects of the classs.
    -Created from the values that are given in the __init__.
    -Can be accessed by using .(dot notation).
    -Can bemodified using the .(dot notation).
    -Use "del" to delete a property from a class.
    