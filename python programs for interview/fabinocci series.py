n=eval(input('enter the number:'))
a=0
b=1
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    print(c,end=' ')



