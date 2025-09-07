#Using a funtion to sum of two numbers ....
#The first part of funtion is defination ....
def toSum(num1 , num2):
    print(num1 + num2)

#to pass all the args in the funtion the type of tuple.....
def tuple(*number):
    print(number , type(number))
    ans = 0
#to print the number indivitualy ....
    for num in number:
        print(num)
#using tuple to sum 
        ans += num
    print(ans)

#The next part is calling that Funtion ....
a = int(input())
b = int(input())
#args
toSum(a , b)
tuple(5 , 3 , a , b)
tuple(a , b)