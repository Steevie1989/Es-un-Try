def AddreversedNum():
    t=int(input(''))
    count =0
    
    if t<=10000:
       while count<t:
           entrie=input('')
           a,b=entrie.split()
           c= a[::-1]
           d= b[::-1]
           e= int(c)+int(d)
           result=0
           while e!=0:
                digit=e%10
                result=result*10 + digit
                e //=10
           print(result)
           count+=1
    return True
AddreversedNum()
