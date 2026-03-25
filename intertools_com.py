#1
from itertools import product
a=[1,2]
b=[3,4]
print(list(product(a,b)))

#2
print(list(product("AB",repeat=2)))

#3
A=[5,6]
print(list(product(A,repeat=3)))

#4
x=[1,2,3]
y=[4,5]
z=list(product(x,y))
print(sorted(z))



#6
from itertools import product
A = [1, 2]
B = [3, 4]
C = [5]
print(list(product(A, B, C)))

#7
from itertools import product
s="abc"
k=2
x=(list(product(s,repeat=k)))
for i in x:
    print("".join(i))



#8
from itertools import product
a=[1,2]
x=(product(a,repeat=3))
for i in x:
    if sum(i)%2==0:
        print(i)

#9
from itertools import product
s="AB"
k=3
x=product(s,repeat=k)
for i in x:
    if i[0]!=i[1] and i[1]!=i[2]:
        print("".join(i))



#5
from itertools import product
s="XYZ"
x=product(s,repeat=2)
for i in x:
    print("".join(i))




#10
from itertools import product
a=[1,2,3]
k=2
for i in product(a,repeat=k):
    if i[0]<i[1]:
        print(i)

