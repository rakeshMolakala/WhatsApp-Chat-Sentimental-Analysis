# Created by C Bharath Sai Reddy
import paralleldots
import matplotlib.pyplot as plt
import numpy as np
import time

# Create a parellel dots account and place the key in the below function

paralleldots.set_api_key( "4YJoR9RToT1Oki3s79ejR8ZBs0trCyZcYNrYHpHp59M" )

f = open("rtest.txt", encoding='cp437')

#f = open("test2.txt", "r")
a=f.read().split("-")
a=a[4:]
x=[]
for i in a:
    z=i.split("\n")
    z=z[0]
    x.append(z)
p=x[0].split(":")
p1=len(p[0])+1
q=x[1].split(":")
q1=len(q[0])+1
#print(p1)
u1=0
u2=0
u1s=[]
u2s=[]
def senti(text):
    dic={}
    time.sleep(1)
    dic=paralleldots.emotion( text )
    dic=dic["emotion"]
    c=[]
    for i in dic.keys():
        c.append(dic[i])
    x=max(c)
    #print(x)
    x=c.index(x)
    #print(x)
    k=0
    for i in dic.keys():
        
        if(k==x):
            return str(i)
        k=k+1
for i in range(len(x)):
    t=x[i]
    t1=t.split(":")
    if(len(t1[0])==p1-1):
        print(t[p1:])
        u1=u1+1
        ss=senti(str(t[p1:]))
        print("Sentiment: ",ss)
        u1s.append(ss)

        
    else:
        u2=u2+1
        print(t[q1:])
        ss2=senti(str(t[q1:]))
        print("Sentiment: ",ss2)
        u2s.append(ss2)
#fig = plt.figure()
def piee(awe):
    labels = list(set(awe))
    sizes=[]
    for i in labels:
        sizes.append(awe.count(i))
    qw=len(sizes)

    colors = ['gold', 'cyan','yellowgreen', 'lightcoral', 'lightskyblue','red']
    colors=colors[:qw]
    #explode = (0.1, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes,labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    #plt.subplot(1,2,1)
    plt.show()
#piee(u1s)
#piee(u2s)
#ax = fig.add_axes([0,0,1,1])
users = [p[0],q[0]]
feq = [u1,u2]
y_pos = np.arange(len(users))
plt.bar(y_pos, feq)
 
# Create names on the x-axis
plt.xticks(y_pos, users)
 
# Show graphic
#plt.subplot(1,2,2)
plt.show()
print(u1s,u2s)
