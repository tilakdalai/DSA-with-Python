# Minimum and Maximum of list elements
n = int(input())
myList = input().split()
for i in range(n):
    myList[i] = int(myList[i])
minimum = myList[0]
maximum = myList[0]
for val in myList:
    if val < minimum:
        minimum = val
    if val > maximum:
        maximum = val
print("Minimum:", minimum)
print("Maximum:", maximum)