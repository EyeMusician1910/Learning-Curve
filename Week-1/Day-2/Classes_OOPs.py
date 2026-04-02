class one:
    x=1;

p1=one();
print(p1.x);

#Setting a default value for an attribute in a class

class Person:
  def __init__(this, name, age=18):
    this.name = name
    this.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

class Person:
    def __init__(ngm, name, age):
        ngm.name = name
        ngm.age = age

    def greet(ngm):
        print("Hello my name is " + ngm.name + " and I am " + str(ngm.age) + " years old.")
p1 = Person("Emil", 36)
p1.greet()

