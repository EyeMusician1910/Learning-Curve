How Code is compiled:
    Code-> Byte OCde->> Python Virtual machine
1> Compile to Byte code
-Byte code runs faster
- .pyc files compiled python files.
# __pycache__-stores all the .pyc files as they can get constantly changed.
    -checks for source code change & also the python version

# PVM: Code loop to iterate byte code,one by one.
    -Byte code isn't machine code. Its python specific interpretation.

# Python shell(IDLE)
    - When a module ius imported,only it's current state will be imported,if chnagesare made,we need to umport it once again.
    -For this use relaod(<file_name>) to reload the import
    -Python treats everything as an object.
    -The variablespoint to the obejct,instead of just fetching the values
    - If an objectwith no reference is found it'll be deleted by the garbage collector in sometime.

# Data types
    -every memory allocation has a refrence count.
    - the datatype is stored wiht the value,not specified by the variable.
    -Slicing makes a copy of the data that is being referred to..
    -{placeholders} are used to add the variables inside a print fucntion.

# Functions
    -Block of that can be used again when we call it

# Arrays Functions 
Method	Description
    append()	Adds an element at the end of the list
    clear()	Removes all the elements from the list
    copy()	Returns a copy of the list
    count()	Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	Removes the element at the specified position
    remove()	Removes the first item with the specified value
    reverse()	Reverses the order of the list
    sort()	Sorts the list

# RegEx
    Function	Description
    findall	Returns a list containing all matches
    search	Returns a Match object if there is a match anywhere in the string
    split	Returns a list where the string has been split at each match
    sub	    Replaces one or many matches with a string

    

