b = [34,21,3,12,34,56,76,5,4,21,12,34]


c = input('Enter The Value:')
k =len(b)
k+=1
b.insert(k,c)
a = 0
for i in b:
    a = a+1

print('count of number is:',a)
print('your list is:',b)

