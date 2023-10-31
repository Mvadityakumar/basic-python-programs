class numbers:
       def min_num(a,b,c):
              minimum=min(a,b,c)
              print(minimum)


       def max_num(a,b,c):
              maximum=max(a,b,c)
              print(maximum)




a,b,c=eval(input('enter the numbers:'))

obj1=numbers
obj1.min_num(a,b,c)
obj1.max_num(a,b,c)



