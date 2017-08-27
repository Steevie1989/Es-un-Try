class Estudiantes:
    def __init__(self,name,lastname,studentid):
        self.name=name
        self.lastname=lastname
        self.studentid=studentid
        self.notas=[]
    def tryit(self):
        print("success")
##    def getname(self):
##        return self.name
##    def getlastname(self):
##        return self.lastname
##    def getstudentid(self):
##        return self.studentid
    def setadress(self,adress):
        self.adress=adress
    def getadress(self):
        return self.adress
    def addnote(self,valor):
        self.notas.append(valor)
    def displaynota(self):
        for a in range(len(self.notas)):
            print('%-12i'%self.notas[a],end='')
    def notafinal(self):
        sum=0
        for a in self.notas:
            sum+=a
        return sum/len(self.notas)
    def displayStudentgrade(self):
        print('{:<12}{:<12}{:<12}'.format(self.name,self.lastname,self.studentid),end='')
        self.displaynota()
        print('%-12s'%self.notafinal())

            
class curso:
    listadeEstudiante=[]
    def __init__(self,coursename,section,term,credit):
         self.coursename=coursename
         self.section=section
         self.term=term
         self.credit=credit
##    def getcoursename(self):
##        return self.name
##    def getsection(self):
##        return self.section
##    def getterm(self):
##        return self.term
##    def getcredit(self):
##        return self.credit
    def matricula(self,student):
        self.listadeEstudiante.append(student)
    def debaja(self,student):
        self.listadeEsudiante.remove(student)
    def cantidad(self):
        return len(self.listadeEstudiante)
        
elestudiante= Estudiantes('Steeven','Petit-Homme',20015275)
elestudiante1=Estudiantes("Patricio","CHamaco",200158456)
elestudiante2=Estudiantes("Jorge","sanchez",200158456)
elestudiante.setadress('Residencia de varones')
inf201=curso("Estructura De Datos",1,'First Semester Fall',3)
inf201.matricula(elestudiante)
inf201.matricula(elestudiante1)
inf201.matricula(elestudiante2)
elestudiante.addnote(92)
elestudiante.addnote(98)
elestudiante.addnote(89)
elestudiante1.addnote(63)
elestudiante1.addnote(77)
elestudiante1.addnote(80)
elestudiante2.addnote(78)
elestudiante2.addnote(83)
elestudiante2.addnote(90)
print(inf201.coursename," section",inf201.section,' ',inf201.term,' credit:',inf201.credit,' Cantidad de estudiantes:',inf201.cantidad())
head=['Name','Lastname','StudentID','Nota1','Nota2','Proyecto','Notafinal']
for a in head:
    print('%-12s'%a,end="")
print()
elestudiante.displayStudentgrade()
elestudiante1.displayStudentgrade()
elestudiante2.displayStudentgrade()
elestudiante.tryit()
##def printnota(estudiante):
##    estudiante.displaynota()
##
##printnota(elestudiante)
