import math
student=['John','Robert','Alfonso']
exams =['Exam1','Exam2','Exam3','Final']
def collectNumbers():
    matrix=[]
    for a in range(3):
        print('Student',a+1,'Nota in one line separated with space')
        #student=[]
       # for b in range(3):
        nota=(input())
        student=[int(b) for b in nota.split()]
        matrix.append(student)
    return matrix
def finalnote(matt):
    sum =0
    for i in matt:   
        sum+=i
    return sum/len(matt) 
def examaverage(matt,valor):
    sum =0
    for i in matt:
        sum+=i[valor]
    return sum/len(i)
def printmatrix(matt):
    a=0
    print('The is the Gradebook of inf201')
    for item in exams:
       print('%19s'%item,end="")
    print()
    for i in matt:
        print('%-11s'%student[a],end =" : ")
        a+=1
        for j in i:
            print('%-19s'%j,end=" ")
        print(round(finalnote(i),2))
    print('%-12s'%'ExamAverage',end=": ")
    for h in range(len(matt)):
        #print("{0:<19}%".format(examaverage(matt,h)),end="")
        print('%-20d'%(examaverage(matt,h)),end="")
        for a in range(len(matt)):
            for b in range(len(matt[a])):
                 print(matt[a][b],end=" ")
            print()     
printmatrix(collectNumbers())
