"""
- In Python anything that you can enclose between single or double quotaion marks is consider as string.
- A string is essentially a sequence or array of textual data. 
- String are used when working with Unicode charcters.

Note:
- It does not matter whether you enclose your strings in single or double quotes, the output remain the same.
- sometimes,the user might need to put quotation marks in between the strings. Example, Consider the sentece: He said, "I want to eat an apple". How will you print this statement in python?: we willl definitely use singl quotes for our convenience
"""
name = "Anuj"
print("Hello, " + name)

print('He daid, "I want to eat an apple"')


# Multiline Strings
"""
- If our string has multiple lines, we can create them like this
"""
a = """Lorem"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# Accessing Character of string
"""
string is like an array of characters. We can access parts of string by using its index which starts from 0. Squre brackets can be used to access element of the string
"""
print(name[0])
print(name[1])
print(name[2])
print(name[3],"\n")

# Looping through the string
"""
we can loop through strings using a for loop like this:

"""
for charcter in name:
    print(charcter)
    
print("*********************************************************")

name1 = "Good morning"
friend = 'Hello'

print("Hi, " + name1)

apple = '''He said,
Hi AK
hey I am Good
"I want to eat an apple.'''

print("lets use a for loop \n")
for charcter in apple:
    print(charcter)