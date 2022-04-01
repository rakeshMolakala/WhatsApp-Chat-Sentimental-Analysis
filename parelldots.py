import paralleldots

# Setting your API key
paralleldots.set_api_key( "4YJoR9RToT1Oki3s79ejR8ZBs0trCyZcYNrYHpHp59M" )

# Viewing your API key
print(paralleldots.get_api_key())
text      = "Chipotle in the north of Chicago is a nice outlet. I went to this place for their famous burritos but fell in love with their healthy avocado salads. Our server Jessica was very helpful. Will pop in again soon!"

paralleldots.abuse( text )
data      =  [ "I like walking in the park", "Don't repeat the same thing over and over!", "This new Liverpool team is not bad", "I have a throat infection" ]
paralleldots.batch_abuse( data )
a={}
a=paralleldots.emotion( text )
a=a["emotion"]
c=[]
for i in a.keys():
    c.append(a[i])
x=max(c)
print(x)
x=c.index(x)
print(x)
k=0
for i in a.keys():
    
    if(k==x):
        print(i)
    k=k+1
    
    
