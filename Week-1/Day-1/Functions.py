def my_function():
  print("Hello from a function")

my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Placeholder functions
def my_placeholder_function():
  pass

#Functions with parameters and return values
def add_numbers(a, b):
  return a + b

#Functions with default parameter values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
my_function(name = "Buddy", animal = "dog")

#Arbitrary arguments
def my_function(*kids):
  print("The youngest child is", kids[2])
my_function("Emil", "Tobias", "Linus")

#Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#args
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#with regular arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
  print("type of names:", type(names))

my_function("Hello", "Emil", "Tobias", "Linus")

#kwargs
def my_function(**kid):
  print("His first name is " + kid["fname"])
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Local Scope- a variable created inside a function is available inside that function
#Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope- a variable created in the main body of the Python code is a global variable
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

#Global Keyword
def myfunc():
  global x
  x = 300
myfunc()
print(x)

#Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
 
#Decorators:Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#Decorator With Arguments
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

#A lambda function is a small anonymous function.

x = lambda a : a + 10
print(x(5))

#better when  an anonymous function inside another function.
#better when used as an argument of a higher-order function (a function that takes in other functions as arguments)
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#lambda used with map()

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Generator Expressions
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#next and yield
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#fibonacci generator
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

#range() function is used to generate a sequence of numbers. It takes three parameters: start, stop, and step. The start parameter is the starting number of the sequence, the stop parameter is the end number of the sequence (exclusive), and the step parameter is the increment between each number in the sequence.

x = range(3, 10, 2)
for n in x:
  print(n)

