import numpy as np
#quest1
l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)
n=int(input("donner un entier:"))
#QUEST2
f=1
for i in range(1,n+1):
    f=f*i
print("le factorielle de"+ str(n) +":",f)
t=int(input("donner un  entier:"))
#QUEST3
dicto={}
for i in range(1,t+1):
    dicto[i]=i*i
print(dicto)
ch=input("donnerchaine:")
index=int(input("donner un entier:"))

res=""
for j in range(len(ch)):
    if j!=index:
        res=res+ch[j]
print(res)
row=int(input("donner un rang:"))
column=int(input("donner une colonne:"))
t=np.zeros((row,column))
print(t)
l=[]
for i in range(row):
    l.append(t[i,:])
print(l)
