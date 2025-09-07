n =int(input())
# m=int(input())

# for currRow in range(n):
#     for currNum in range(m):
#         print(currNum+1 , end=" ")
#     print("  ")


for currRow in range(n):
    for currNum in range(n):
        if currNum <= currRow:
            print(currNum+1 , end=" ")
        else:
           break
    print(" ") 

