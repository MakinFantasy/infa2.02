k = 0
for n in range(174457, 174506):
    list_del = []
    for d in range(2, n//2 + 1):
        if n % d == 0:
            list_del.append(d)
            if len(list_del) > 2:
                break
    if len(list_del) == 2:
        print(list_del[0], list_del[1])