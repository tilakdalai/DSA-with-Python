n =int(input())

for currRow in range(n):
    for currNum in range(n):
        if (currNum < n-(currRow+1)):
            print(" " , end=" ")
        else:
            print("*" , end=" ")
    print(" ")            
