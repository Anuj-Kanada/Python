"""
We can take user input directly using input() function. This input function gives return value as string/charcter hence we have to pass that into  a variable

    sysntax: variable = input()

but this input function return the value as string. Hence we ave to typecast them whenever required to another datatype.
    variable = int(input())
    variable = float(input()) 

We can also display a text using input function. This will make input() function take user input and display a message as well.
"""
a = input("Enter your name: ")
print("My name is", a)

x = int(input("Enter first number: "))
y = input("Enter Second Number: ")

print(x + int(y))
