i=1
while i<=10:
    print(i,end="   ")
    i+=1
print()


for i in range(1,11):
    print(i,end="   ")
print()

name="Darshan"
for index ,i in enumerate(name):
    print(f"for \'{i}\' at {index}index ")
print()

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()
print()

for i in range(1,31):
    if i%3==0:
        print(i,end=" ")
print()

for i in range(1,10):
    print(i+i,end=" ")
print()

names="Darshan"
for name in names:
    print(name)

name="Darshan"
vowels="aeiouAEIOU"
count=0
for i in name:
    if i in vowels:
        count+=1
print("Vowels:",count)
print()