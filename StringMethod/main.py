#Strinf are Immutable
a = "Anuj"
print(len(a))
print(a.upper())
print(a.lower())

b = "Harry!!!!!!!!!!"
print(b.rstrip("!"))

c = "@@@@ Anuj"
print(c.lstrip("@"))

print(a.replace("Anuj", "Kanada"))

k ="Anuj Kanada 2110" 
print(k.split())      # convert or we can say split the string into list

c = "i Am anuj Kanada"
print(c.capitalize())

m ="Welcome to the console!!!"
print(len(m))
print(m.center(50))
print(len(m.center(50)))

print(m.count("Welcome"))
print(m.count("welcome"))

str1 = "Welcome to python !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str = "He's name is Dan. He is man honest man"
print(str.find("is")) # it give occurence 
print(str.find("ishh")) # it give -1 value 
# if value not match then find give -1 and index throw an error
#print(str.index("ishh")) # it throw error

str2 = "WelcomeToTheConsole"
print(str2.isalnum())

str3 = "Welcome00"
print(str3.isalpha())
print(str3.islower())

s = "This is Anuj"
print(s.isprintable())

s1 = "This is Anuj\n"
print(s1.isprintable())

s2 = "         " # using spacebar or tab
print(s2.isspace())

str4 = "I Am Anuj Kanada"
print(str4.istitle())

Str5 = "I Am Anuj"
print(Str5.swapcase())

print(str4.startswith("Anuj"))

f = "his name is Dan. and Dan is an honest man."
print(f.title())
