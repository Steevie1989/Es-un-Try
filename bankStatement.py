import datetime
import random
import math
class Client:
    def __init__(self,name,lastname,adress,cell,socialS):
        self.name=name
        self.lastname=lastname
        self.adress=adress
        self.cell=cell
        self.socialS=socialS
        self.depot=[]
        self.withdrawal=[]
    def setAdress(self,newadress):
        self.adress=newadress
    def setcell(self,newcell):
        self.cell=newcell
    def accountNumber(self):
        code= '021'
        ran=random.randint(100,999)
        ss=self.socialS[9:]
        return code + ss + str(ran)
    def deposit(self,number):
        self.depot.append(number)
    def getdeposit(self,a):
        if a > len(self.depot)-1:
            return 0
        return self.depot[a]
    def totalDeposit(self):
        sum=0
        for a in self.depot:
            sum+=a
        return sum
    def withdraw(self,number):
        self.withdrawal.append(number)
    def getwithdraw(self,a):
        if a > len(self.withdrawal)-1:
            return 0
        return self.withdrawal[a]
    def totalwithdraw(self):
        sum=0
        for a in self.withdraw:
            sum+=a
        return sum      
    def balance(self,a):## not correct
        bal= self.getdeposit(0)- self.getwithdraw(0)
        b=a+1
        bal+=self.getdeposit(b)
        bal-=self.getwithdraw(b)  
        return bal
      
    def transactionCode(self,a):
        code=random.randint(1001,100000000)
        return code    
    def transactionDate(self):
        date = datetime.date.today()
        return date
    def bankstatement(self):
        dash()
        print('%-103s|'%'|Marvel&co cooperative')
        print('%-103s|'%'|787-488-2143')
        print('%-103s|'%'|Santurce PR 00914')
        print('|%90s%12s|\n|%102s|\n|%102s|' %(self.name,self.lastname,self.cell,self.adress))
        print('|%103s'%'|')
        print('%s%15s%74s'%('|Bank Statement','June-july 2017','|'))
        print('%s%s%78s'%('|Account Number: ',self.accountNumber(),'|'))
        print('|%103s'%'|')
        dash()
        head=['|Fecha','Transactioncode|','Withdraw|','Deposit|','balance|']
        dash
        for i in head:
            print('{:24}'.format(i),end='')
        print()
        dash()
        for a in range(len(self.withdrawal) + len(self.depot)):
           print('|{}|{:27}|{:16,.2f}|{:22,.2f}|{:23,.2f}|'.format(self.transactionDate(),self.transactionCode(a),self.getwithdraw(a),self.getdeposit(a),self.balance(a)),end='')
           print()
           dash()
    #print(juneTransaction.transactionDate(),juneTransaction.transactionCode(),juneTransaction.withdraw(),juneTransaction.deposit(),juneTransaction.balance())

class TransactionPeriod:
    clientlist=[]
    def __int__(self):
        self=null
    def addClient(self,unclient):
        self.clientlist.append(unclient)
client1=Client('Steeven','Petit-Homme','Residencia Sagrado Corazon','784227643','0002-98-9898')
juneTransaction=TransactionPeriod()
juneTransaction.addClient(client1)
client1.deposit(1823.23)
client1.deposit(200)
client1.withdraw(500)
client1.deposit(2000)
client1.withdraw(400)
client1.withdraw(20)
client1.withdraw(40)
client1.withdraw(423.44)
client1.withdraw(20)
def dash():
    print('+',end='')
    for a in range(102):
        print('-',end='')
    print('+')
    
client1.bankstatement()
        
    
