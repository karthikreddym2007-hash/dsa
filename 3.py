def myfun(fname):
    print(fname + "hello")

myfun("karthik  ")
myfun("sai  ")

def my_function(name): 
  print("Hello", name)

myfun("Emil") 

def my_functionn(fname, lname):
  print(fname + " " + lname)

my_functionn("Emil", "Refsnes")


def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


def ani_name(animal , name):
    print("I have a " + animal)
    print("I have a " + animal + " name is " + name)

ani_name("goat", "vk")


def my_function(fruits):
  for i in fruits:
    print(i)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)



def my_fun(x,y):
    return x+y

print(my_fun(5,3))


def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

