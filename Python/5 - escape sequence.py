"""
# Escape Sequence Characters
To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

"""

print("I am \n Anuj Kanada")
print("I am \"Anuj Kanada\"")


"""
we can give multiple value in print
print(object(s), sep=separator, end=end, file=file, flush=flush)

Other Parameters of Print Statement:

- object(s): Any object, and as many as you like. Will be converted to string before printed
- sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
- end='end': Specify what to print at the end. Default is '\n' (line feed)
- file: An object with a write method. Default is sys.stdout

"""
print("HEY", 6, 7, sep="~")

print("Hello World", end="hi")
print("good Morning")

print("Good Afternoon", end = "4.00\n")
print("evening Good")
