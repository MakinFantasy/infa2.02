k = 0
for i in range(77777777, 88888889):
    list_del = []
    for j in range(2, i//2 + 1):
        if i%j == 0:
            if j % 2 != 0:
                list_del.append(j)
    if len(list_del) == 5:
        print(i, min(list_del), list_del)
