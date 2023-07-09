f1=open("EMP1.csv","r")
f2=open("empsal.csv","r")
f3=open("DATA.csv","w")

edata=f1.read()
esal=f2.read()

elst=edata.splitlines()
slst=esal.splitlines()

for line1 in elst:
    word1=line1.split(",")
    for line2 in slst:
        word2=line2.split(",")
        if (word1[0]==word2[0]):
            line1=line1+","+word2[1]+","+word2[2]+"\n"
            f3.write(line1)

f1.close()
f2.close()
f3.close()

#NEXT

from datetime import datetime

f1=open("DATA.csv","r")
c=f1.read()
dat=c.splitlines()

no=[]
name=[]
des=[]
add=[]
sal=[]
dob=[]

for line in dat:
    word=line.split(",")
    no.append(int(word[0]))
    name.append(word[1])
    des.append(word[2])
    add.append(word[3])
    sal.append(int(word[4]))
    dob.append(word[5])

print("max salary ",name[sal.index(max(sal))],max(sal))
print("min salary ",name[sal.index(min(sal))],min(sal))
print("avg salary ",((sum(sal))/len(no)))

today=datetime.today()

for d in dob:
    ed=datetime.strptime(d,'%m/%d/%Y').date()
    print("age of employee ",(today.year-ed.year))

for s in sal:
    sd=s/82
    print("salary in dollars ","$",sd)
