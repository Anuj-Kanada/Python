for i in range(12):
    if(i == 10):
        break   #Skip the Loop
    print("5 X", i+1, '=', 5 * (i+1))


print("Come our from loop") 

for i in range(12):
    if(i == 10):
        print("Skip the Iteration")
        continue
    print("5 X", i, '=', 5 * i)

    # Emulate Do While
    while True:
        print(i)
        i = i + 1
        if(i % 100 == 0):
            break
        

