'''
153
1**3 + 5**3 + 3**3
'''


def armstrong(n):


    le=str(n)         #converstion int to string
    length=len(le)    #find the length of string

    temp = n
    sum=0
    while temp>0:
       digit=temp%10
       sum+=digit**length
       temp//=10   #increment the while by division
    if n==sum:
       print('armstrong')
    else:
       print('not armstrond')
n = eval(input('enter the number:'))


armstrong(n)




























