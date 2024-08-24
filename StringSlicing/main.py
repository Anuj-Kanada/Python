name = "Anuj, kanada"
print(name[0:5])
print(len(name))

fruit = "Mango"
len1 = len(fruit)
print("mango is a", len1, "letter word." )

#Slicing
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # it start from first digit but not going to the last digit
print(fruit[1:4]) # including 0 but not 4
print(fruit[:5]) 
print(fruit[0:])
print(fruit[0:-3]) # it take like len(fruit)-3 = 5 - 3 = 2 -> print(fruit[0:2]) =  Ma

print(fruit[-1:-3]) # it mean [4:2] 
print(fruit[-3:-1]) # it mean [2:4]

nm = "Harry"
print(nm[-4:-2])