myList = []
n = int(input("Enter number of elements to be added in the list: "))
for i in range(n):
    element = int(input("Enter element: "))
    myList.append(element)
print("The list is:", myList)
print("The length of the list is:", len(myList))
print("The first element is:", myList[0])
print("The last element is:", myList[-1])
print("The second last element is:", myList[-2])
print("The type of the list is:", type(myList))

# Define a list with different data types using input
myList2 = input().split()
print(myList2 , type(myList2), len(myList2))
#typecasting the elements to int
for i in range(len(myList2)):
    myList2[i] = int(myList2[i])
print(myList2 , type(myList2), len(myList2))