#Fibonnacci number using recurssion 
def fiboo(n):
    if n==1 or n==0:
        return 1
    return fiboo(n-1) + fiboo(n-2)

a = int(input())
ans = fiboo(a)
print(ans)