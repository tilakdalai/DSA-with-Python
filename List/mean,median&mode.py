n = int(input("Enter number of elements: "))
myList = input("Enter the elements separated by space: ").split()
#mean = sum of all values / number of values
sumofList = 0
for val in myList:
    sumofList += int(val)
mean = sumofList / len(myList)
print("Mean:", mean)
#median = middle value in a sorted list
for i in range(n):
    myList[i] = int(myList[i])
myList.sort()
if n % 2 == 1:
    median = myList[n // 2]
else:
    median = (myList[n // 2 - 1] + myList[n // 2]) / 2
print("Median:", median)
print("Sorted List:", myList)
#mode = value that appears most frequently
maxCount = 0
maxEle = myList[0]
for currEle in myList:
    count = 0
    for val in myList:
        if val == currEle:
            count += 1
    if count > maxCount:
        maxCount = count
        maxEle = currEle

print("Mode:", maxEle , "appears", maxCount, "times")