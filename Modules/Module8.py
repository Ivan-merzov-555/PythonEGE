import itertools
alphabet = "0123456789"
ar = itertools.permutations(alphabet, 6) #Размещение
arl = []
for e in ar:
    arl.append(list(e))
count = 0
for e in arl:
    flag = True
    for i in range(len(e)-1):
        if (e[0] == "0") or (int(e[i]) % 2 == 0 and int(e[i+1]) % 2 == 0) or (int(e[i]) % 2 != 0 and int(e[i+1]) % 2 != 0) or (e[5] != "5" and e[5] != "0"):
            flag = False
    if flag:
        count += 1
print(count)