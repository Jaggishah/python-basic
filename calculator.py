print('Write 1 For Addtion,2 for substraction, 3 for multiplication ,4 for division and 5 for float divide')
b=input('enter Your Choice-')
if(b=='1'):
    x=input('enter you first number')
    y=input('enter your second number')
    
    print('result is =',int(x)+int(y))
elif(b=='2'):
    x=input('enter you first number')
    y=input('enter your second number')
    
    print('result is =',int(x)-int(y))
elif(b=='3'):
    x=input('enter you first number')
    y=input('enter your second number')
    
    print('result is =',int(x)*int(y))
elif(b=='4'):
    x=input('enter you first number')
    y=input('enter your second number')
    
    print('result is =',int(x)/int(y))

elif(b=='5'):
    x=input('enter you first number')
    y=input('enter your second number')
    
    print('result is =',float(x)/float(y))
else:

    print('your output is wrong')

