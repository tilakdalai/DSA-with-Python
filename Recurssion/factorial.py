#factorial of a number using itresion......
# n = int(input())

# ans = 1
# for i in range(1 , n+1):
#     ans *= i
# print(ans)

#factorial of a number using reurssion......
def fact(n):
    if n==1 or n==0 :
        return 1
    return n * fact(n-1)

n = int(input())
a = fact(n)
print(a)
