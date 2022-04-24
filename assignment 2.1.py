a = [1,'f',2,'b',3,4,'h','j',6,9,0,'k']
print('This Is  The List What You Want To Seperate=',a)

l = 0
for i in a:
    if(a.index(i) > 1):
      x = int(a.index(i))
      n = []
      n.insert(l,x)

       

           
    else:
        print('Entered Data Is NOt Valid.')

print('First List is:',n)


        


