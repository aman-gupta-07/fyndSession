def display():
    return 0


display()
# Won't display any output.
# Return type parametric functions


def display():
    return 100


display()
# Won't display any output.

# Parametric Functions for printing the  result.


def add(x, y):
    return x + y


print(add(3, 4))


def add(x, y):
    print(x + y)


add(3, 4)
# Using Print won't give us access
# for the function any further suppose we want to use add(a, b) anywhere else.

# Parametric functions  with more parameters and less arguments


def add_special(num1, num2, num3=100):
    print(num1 + num2 + num3)


add_special(10, 20, 30)
add_special(10, 20)


# Parametric functions with less parameters and more arguments will give us an error
# for providing less no. of arguments.

def doSomething(a, b, c):
    print(a*b + b*c + c*a)


# doSomething(10, 20) : Missing 1 required positional argument: 'c'
doSomething(10, 20, 30)
# returns 1100
# def infVal1(*num1, num2):
#  print(num1)
#  print(num2)


# infVal1(10, 20, 30, 40)
# Error as num1 will take whole arguments
# Function Declaration
def declareFun():
    pass


# Arguments with Parameters names
def func1(num1, num2):
    print("num1 :", num1)
    print("num2 :", num2)


func1(num2=10, num1=20)
# In Static languages
# void declareFun();


def infVal2(*num1, num2=30):
    print(num1)
    print(num2)


infVal2(10, 20, 30, 40)
infVal2()
# First argument will go for num1 and others
# will go for num2 and output will be in the form of a tuple


def infVal(num1, *num2):
    print(num1)
    print(num2)


infVal(10, 20, 30, 40)


def infVal3(num2=30, *num1):
    print(num1)
    print(num2)


infVal3(10, 20, 30)
# infVal3(num1 = 10, 20)


# Comparing Functions with other languages
def add(a, b):
    print(a+b)


# void add(int a, int b)
# {
# print(a + b);
# }

# With Python we can take different types of arguments in add function
# like int, int and int, float and float, float and float, int and str, str or
# other data types which can be concatenated
# But in other languages this is not possible.
# But at the same time time complexity for Python is much more
# in comparison to other languages


# SyntaxError: non-default argument follows default argument
# def infVal4(num1=30, num2):
#   print(num1)
#   print(num2)

# infVal4(10)

def outSide(p1, p2):
    def inside(p3, p4):
        return p3*p4

    result = inside(p1, p2) - 10
    print(result)


# outSide(10, 20)


var = 100


def do_something():
    global var
    var = 20


do_something()
print(var)
