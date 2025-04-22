"""
# Length of a String
- we can find length using len() Function
"""
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

"""
# String as an array
- A String is essentially a sequence of character also called an array. Thus we can access the element of this array.
"""
pie = "ApplePie"
print(pie[:5])
print(pie[6]) #returns character at specified index

"""
Note : This method of specifying the start and end index to specify a part of string is calle slicing.
"""
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative , index len(pie)- 8 = 0


"""
# Strings are array and array are iterable. Thus we can loop through strings.
"""
alphabets = "ABCDE"
for i in alphabets:
    print(i)
    
print("****************************************************************************")

fruit =  "Mango"
mangoLen = len(fruit)
print(fruit[0:4]) # incluidng 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

"""
# Note: fruit[-1:2]  → fruit[4:2]  → default step is +1
        [start:end:step]
        fruit[4:1:-1]  # returns 'og'
        
start=4 ('o'), end=1 ('a'), step=-1

This gives: index 4 → 3 → 2 (but stops before reaching 1)

Result: 'o' + 'g' → 'og'

You are slicing from index 4 to index 2 (since -1 refers to index 4 in "Mango"), but slicing in Python goes left-to-right by default, unless you explicitly give a negative step.

Since start > end and step is positive → this returns an empty string.
"""