class Complex:
    def __init__ (self,real,i):
        self.real =real
        self.i=i
       # self.issquare=True
    def getre(self):
        return self.real
    def getim(self):
        return str(self.i)+'i'
    def __add__(self,other):
        newreal = self.real + other.real
        newi=self.i + other.i
        return Complex(newreal,newi)
    def __mul__(self,other):
        newareal = self.real * other.real - self.i * other.i
        newi=self.real * other.i + self.i * other.real
        return Complex(newareal,newi)
    def __sub__(self,other):
        newareal = self.real - other.real
        newi=self.i - other.i
        return Complex(newareal,newi)
    def __str__(self):
        if self.real ==0 and self.i==0: # si real es nulo y imaginario es nulo
            return '0' # el numero complejo es nulo
        if self.real==0: # si real es nulo
            return str(self.i) + 'i' # solo existe la parte imaginaria
        elif self.i==0:# si imaginario es nulo
            return str(self.real) # solo existe la parte real
        elif self.i<0: # si la parte imaginaria es negativa 
            return str(self.real)  +  str(self.i) +'i' #conservamos el signo negativo
        else: # en caso contrario devuelve el formato completo
            return str(self.real) + ' + ' + str(self.i) +'i'
    def __truediv__ (self,other):
        den = other.real * other.real + other.i * other.i
        if den ==0: # si el denominador es negativo
            return Complex(0,0) # se anula el numero complejo
        else: 
          newreal = (self.real * other.real + self.i * other.i)/den
          newi = (self.i*other.real - self.real*other.i)/den
        return Complex(newreal,newi)
    def conjugate(self):
        changedsigne=-self.i
        if changedsigne<0:
            return str(self.real) + str((changedsigne))
        else:
            return str(self.real) + '+'  + str((changedsigne))
    def __eq__(self,other):
        if self.real==other.real and self.i==other.i:
            return True
        else:
            return False

f1=Complex(2,-4)
f2=Complex(5,-10)
print('f1---->real =',f1.getre())
print('f1---->image =',f1.getim())
print('f2---->real =',f2.getre())
print('f2---->image =',f2.getim())
print('Equality =',f1==f2)
print('f1 conjugate',f1.conjugate())
print('f2 conjugate',f2.conjugate())
print()
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

