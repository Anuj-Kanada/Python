#Default Argument
def average(a = 5 , b = 5):
    print("The Average is", (a + b)/2)
average()

average(a = 5, b = 6)

average(a = 8)

average(b = 9)

#Keyword Argument -> we can chjage the eorder of argument
average(b = 11, a  = 10)

#require Argument

def averages(a , b = 5):
    print("The Average is", (a + b)/2)
averages(a=1)

#variable length argument
def plus(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))
    # return 7
    return sum/len(numbers)

plus(5, 6, 7, 1)
c = plus(1,2,3,4,5,6,7,8,9,10)
print(c) 
