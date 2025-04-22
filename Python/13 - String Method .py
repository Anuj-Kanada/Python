# Srings are Immutable
"""
 python provide sets of built-in methods that we can use to alter and modify the strings.

"""
# upper(): The upper() method convert a string to upper case
str1 = "AbcDEfghIJ"
print(str1.upper())

print(str1.lower())

#Strip(): method removes any whitespaced before and after the string
str2 = " Silver Spoon "
print(str2.strip())

#rstrip(): rmeoves any trailing charcters
str3 = "Hello !!!"
print(str3.rstrip("!"))

# replace(): method replace alll occurence of a string with another string
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

#split(): method split the given string at the specified instance and returns the separated strings as list items.

str2 = "Silver Spoon"
print(str2.split(" ")) # Splits the string at the whiteapace " ".

# capitalize() : method turn on;y the first charcter of string to uppercase and the rest other charcter of the string are turned to lowercase. The string has no effect if thr first charcter is alredy uppercase.

str1 = "Hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)


# center(): methos aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50))

# We can also provide paddeing charcter, it will fill the rest of the fill charcter provided by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

# count(): methods returns the number of times the given value has occured within the given string.

str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

# endswith(): method checks if the string ends with a given value, If yes then return True, else return false.
str1 = "welcome to the console !!!"
print(str1.endswith("!!!"))

# we can even also check for a value in-between the string by providing strat and end index positions.
str1 = "Welcome to the console !!!"
print(str1.endswith("to", 4, 10))

#find(): method searches fro the first occurence of the given value and returns the index where it is prevent. if given value is absent from the string then return -1.

str1 = "He's name is dan. He is an honest man."
print(str1.find("is"))

# as we can see, this method is somewhat similar to thr index() method. The major differnece beign that index() raises an exception if value is asent whereas find() does not.
str1 = "He's name is dan, He is an honest man."
print(str1.find("dani"))

#index(): method searchesfor te first occurence of the givrn value and return the index where it is present. If given value is absent from the string then raise an exception.
str1 = "He's name is Dan. Dan is an honest man"
print(str1.index("Dan"))

# As we can see, this method is domewhat similar to the find method. the major differnce being that index()raise an exception if valur is absent whereas find() does not.
# str1 = "He's name is Dan. Dan is an honest man"
# print(str1.index("Daniel"))

#isalnum: method returns true only if the entire string only consist of A-Z,a-z, 0-9. is any other charcter or punctuations are present, then it returns false.

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

#isalpha(): method return True only if the entire string only consists of A-Z, a-z. If anu other charcter or punctuations os numbers(0-9) are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())

# islower(): method returns true if all the charcters in the string are lower case. else it returns False.
str1 = "hello world"
print(str1.islower())

#isPrintable(): method returns True if all the values within the givrn string are printable, if not, then return Flase.
str1 = "we wish you a very Merry Christmas"
print(str1.isprintable())

# isspace(): method returns True only and only if the string contain white space, else returns false

str1 = "            " # using spacebar
print(str1.isspace())
str2 = "            " # using tab
print(str2.isspace()) 

# istitle(): returns True only if the first letter of esch word of the string is capitalized, else it returns Fasle.
str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

# isupper(): method returns True if all the charcters in the string are upper case, else it returns false.
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())

# startswith() : method checks if the string starts with a given value. if yes then return True, else return false.
str1 = "python is a Interpreted Language"
print(str1.startswith("python"))

#swapcase() : The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

# title(): method capitalize each letter of the word within the string.
str1 = "He's name is Dan. Dan is an Honest man"
print(str1.title())
