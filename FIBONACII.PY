#fibonacci
f1=0
f2=1
for i in range(0,10):
    tot=f1+f2
    f1=f2
    f2=tot
#    print(tot)

#Prime Numbers
num=int(input(""))
for y in range(2,num):
    if num % y == 0:
        print('not prime')
    else:
        print('Prime')

