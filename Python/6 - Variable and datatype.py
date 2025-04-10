# Everything in python are object
"""
# Variable

- Variable is like a container that holds data. 
- Creating a variable is like creating a placeholder in memory and assigning it some value.
"""
a = (3,2)
print(type(a), a)
b = True
print(type(b), b)
c = "Harry"
print(type(c), c)
d = None
print(type(d), d)
E = 1
print(E, type(E), sep="->")

"""
# Datatype

* Mutable -> Changeble
* Immutable -> Unchangeble

- Datatype Specifies the type of the value a variable hold.
- in python we can know the value of the variable using type function

1. Numeric Data: int, float, complex
    - int : 3, -8, 0
    - float: 7.349, -9.0, 0.00001
    - complex: 6+2i
    
2. Text data: String
    - str: "Hello World!", "127", 3.8
    
3. Boolean data: It Consists of True and False.

4. Sequenced Data: List, Tuple
    - list: A list is an order collection of data with element seprated by a comma and enclosed within squre brackets. List are murable and can be modified after creation.
    - tuple: A tuple is an order collection of data with element seprated by a comma and enclosed within parentheses. Tuple are Immutable and can not be modified after creation.

5. Mapped data: Dictionary
    -   dict: A dictionary is an unorder collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
"""
list1 = [8, 2.3, [-4, 5], ["apple", "Banana"]]
print(list1, type(list1))

tuple = (("parrot", "sparrow"), ("lion", "Tiger"))
print( type(tuple),tuple)

dict = {"name":"Anuj Kanada", "age":22, "canVote":True}
print(type(dict), dict)