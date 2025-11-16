#sum of list elements
n = int(input())
myList = input().split()
sumofList = 0
for i in range(n):
    sumofList += int(myList[i])
print(sumofList)

# Alternative approach 
m = int(input())
myList2 = input().split()
for i in range(m):
    myList2[i] = int(myList2[i])
print(sum(myList2))