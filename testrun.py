
import paralleldots

# Setting your API key
paralleldots.set_api_key( "4YJoR9RToT1Oki3s79ejR8ZBs0trCyZcYNrYHpHp59M" )

f = open("test2.txt", encoding='cp437')
#print(f.read())
#f = open("test2.txt", "r")
a=f.read().split("-")
a=a[4:]
x=[]
#print(a)
for i in a:
    z=i.split("\n")
    z=z[0]
    x.append(z)
p=x[0].split(":")
p1=len(p[0])+1
q=x[2].split(":")
q1=len(q[0])+1
print(p1)
print(q1)

    

