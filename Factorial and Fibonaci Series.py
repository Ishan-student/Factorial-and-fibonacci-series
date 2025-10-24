#Ishan Maurya
#29/08/2025
#PU023223EUGBTAR026
#Factorial and Fibonaci Series
print('Ishan Maurya')
fact=1
n=int(input('Enter the number to get factorial:  '))
for i in range(1,n+1):
    fact=fact*i
    
print('Factorial of',n,'is ',fact)

print('*'*100)

print('Fibonacci Series')
a=0
b=1
print(a)
print(b)
for i in range(0,n-2):
    c=a+b
    print(c)
    a=b
    b=c
    
