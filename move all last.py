x = [1, 3 , 0 , 2, 4, 0, 5, 0, 6, 7, 0, 8, 0, 9]

result = []
for i in x:
    if i != 0:
        result.append(i)
for i in x:
    if i == 0:
        result.append(i)
print(result)