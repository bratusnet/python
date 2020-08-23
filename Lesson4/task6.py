from itertools import cycle, count, repeat

# список a
l=[]
for el in count(3):
    if el > 10:
        break
    else:
        l.append(el)

print(f"Полученный список а) : {l} \n")

# список b
с = 0
l2=[]
for el in cycle(l):
    if с > 31:
        break
    l2.append(el)
    с += 1
print(f"Полученный список b) : {l2} ")
