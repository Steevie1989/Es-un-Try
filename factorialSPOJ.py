##def factorial(num):
##    factorial=1
##    for a in range(1,num+1):
##        factorial*=a
##    return factorial
##def trailingZero1(num):
##    t= str(factorial(num))
##    q=t[::-1]
##    count=0
##    for a in q:
##        if a=='0':
##            count+=1
##        else:
##            break
##    print(count)
def trailingZero(num):
    t=0
    for a in range(1,num):
        if 5**a> num:
            break
        else:
            t+=num//5**a
    print(t)
    return True
loop=0
T=int(input(''))
if T<=100000:
      while loop<T:
          num=int(input(''))
          if num<=1000000000 and num!=0:
                trailingZero(num)
          loop+=1
