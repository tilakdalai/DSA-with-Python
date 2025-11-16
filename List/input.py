mylist = []
n = int(input("Enter number of elements to add to the list: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    mylist.append(element)
print("List after input:", mylist)
mylist1 = input()
#it will take the input as a string
print("You entered:", mylist1)
print("Type of the entered input:", type(mylist1))
mylist1 = mylist1.split() #it will split the string based on space and return a list
print("List after splitting the input string:", mylist1)