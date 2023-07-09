f=open("sales.csv","r")
data=f.read()
lines=data.splitlines()
pdetails=[]
sdetails={}
gdetails={}
ctemp=[]
Pfc={}
Sfc={}
Cfc={}
male=0
female=0
for l in lines:
words=l.split(",")
pdetails.append(words[1])
ctemp.append(words[3])
sdetails[words[0]]=words[2]
gdetails[words[3]]=words[4]
for p in pdetails:
if p not in Pfc:
Pfc[p]=1
else:
Pfc[p]=Pfc[p]+1
max=0
Pn=""
for k,v in Pfc.items():
if(max<v):
max=v
Pn=k
print("Most popular product is: ",Pn)
for c in ctemp:
if c not in Cfc:
Cfc[c]=1
else:
Cfc[c]=Cfc[c]+1
max=0
Cd=""
for a,b in Cfc.items():
if(max<b):
max=b
Cd=a
print("Customer who buys most of the products is: ",Cd)
for k,v in gdetails.items():
if(v=="female"):
female=female+1
else:
male=male+1
print("Number of customers who are female are: ",female)
OUTPUT-
