given=int(input('enter:'))
s=str(given)
reverse=s[::-1]
print(int(reverse))
#or
given=int(input('enter:'))
rev=0
while(given>0):
    y = given % 10
    rev=rev*10+y
    given=given//10
print(rev)




