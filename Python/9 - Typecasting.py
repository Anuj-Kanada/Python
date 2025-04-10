"""
# Typecasting
- The Conversion of one datatypr into the other data type is known as type casting or type conversion in python
- Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for        the  type casting in python.

Two Types of Typecasting:

1. Explicit Conversion (Explicit type casting in python):
    - The conversion of one data type inyo  another datatype, done via developer or programmer's intervention or manually as per the requiremnt is known as ....
    
    - it can be achieved with the help of python's built-in typr conversion function such as int(), float(), hex(), oct(), str()
    

"""

# Explicit
string = "15"
number = 7
string_number = int(string) # throe an error if the string is not a valid integer
sum = number + string_number
print("The sum of the both number is:", sum)


"""
2. Implicit Conversion (Implicit type casting in python)
    - Data type in python do not have same level i.e. ordering of data types is not the same in python.
    
    - Some of the datatype have higher-order and some have lower order, while performing any operations on variable with different datatypes in python, one of the varialbe's datatype will be changed to yhe higher datatype. According to the level, one datatype is converted into other by the python interpreter itself(automatically), This is called implicit typecasting in python.
    
    - Python converts a smaller datatype to a higher data type to prevent data loss.

"""
# Implicit

# python automattically converts
# a to int
a = 7
print(type(a))

# python automatically converts b to float
b = 3.0
print(type(b))

# python automatically convert c to float as it is a float addition
c = a + b
print(c)
print(type(c))


print("************************************************************")
#explicit
a = "1"
# a = 1
b = "2"
# b = 2

print(int(a) + int(b))

# Implicit Typecasting
c = 1.9
d = 8
print(c+d)