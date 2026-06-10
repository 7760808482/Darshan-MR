import random
password_length=int(input("Enter the Length of the Password:"))
str1="QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq1234567890-=!@#$%^&*()_+"
password_list=[]
for i in range(password_length):
    pa=random.choice(str1)
    password_list.append(pa)
password=""
for i in password_list:
    password+=i
print(password)