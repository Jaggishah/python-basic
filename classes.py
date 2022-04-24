class jaggi:
    def __init__(a,name,age):
        a.j=name
        a.k=age
    def main(a):
        print('this is a main')
class shah(jaggi):
    def __init__(a, name, age):
        super().__init__(name, age)
        a.l =name

n =jaggi("jaggi",19)
print(n.j,n.k)
n.main()

print(n.l)
        