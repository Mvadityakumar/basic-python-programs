class star:
    def left(n):
        for i in range(1, n + 1):
            print(i * '*')



    def square(n):
        for i in range(1,n+1):
            print('*'* n)




    def fun1(n):
        for i in range(1,n+1):
            for j in range(i):
                print('*',end='')
            print()

    def fun2(n):
        for i in range(n,0,-1):
            for j in range(i):
                print('*',end='')
            print()


    def fun3(n):
        for i in range(1,n+1):
            for j in range(i):
                print(i,end='')
            print()

    def fun4(n):
        for i in range(n,0,-1):
            for j in range(i):
                print(i,end='')
            print()

    def fun5(n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end='')
            print()

    def fun6(n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end='')
            print()

    def fun7(n):
        for i in range(1,n+1):
            for j in range(n,i,-1):
                print(' ',end='')
            for k in range(1,i+1):
                print('*',end='')
            print()

    def fun8(n):
        for i in range(n,0,-1):
            for j in range(n,i,-1):
                print(' ',end='')
            for k in range(1,i+1):
                print('*',end='')
            print()

    def fun9(n):
        for i in range(1,n+1):
            for j in range(n,i,-1):
                print(' ',end='')
            for k in range(1,i+1):
                print(k,end='')
            print()

    def fun10(n):
        for i in range(n,0,-1):
            for j in range(n,i,-1):
                print(' ',end='')
            for k in range(1,i+1):
                print(k,end='')
            print()

    def fun11(n):
        s=0
        for i in range(n):
            for j in range(i+1):
                print(s,end=' ')
                s+=1
            print()
n=eval(input('enter the number:'))

obj1=star
obj1.left(n)
print()
obj1.square(n)
print()
obj1.fun1(n)
print()
obj1.fun2(n)
print()
obj1.fun3(n)
print()
obj1.fun4(n)
print()
obj1.fun5(n)
print()
obj1.fun6(n)
print()
obj1.fun7(n)
print()
obj1.fun8(n)
print()
obj1.fun9(n)
print()
obj1.fun10(n)
print()
obj1.fun11(n)
