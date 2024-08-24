def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a, b):
    if(a > b):
        print("First number is Greater than Second")
    else:
        print("Second number is Greater than First")
    
def isLesser(a, b):
    pass

a = 9
b = 8
# gmean = a*b/(a+b)
# print(gmean)
isGreater(a, b)
calculateGmean(a, b)

c = int(input("Enter The number for C: "))
d = int(input("Enter The number for B: "))
# gmean1 = (c*d)/(c+d)
# print(gmean1)
isGreater(c, d)
isLesser(c, d)    
calculateGmean(c, d)
