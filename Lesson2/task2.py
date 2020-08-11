lst = list(input("Введите список элементов: "))
print(lst)
l=len(lst)
if l%2==0:
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        lst2=list(''.join([str(i) for i in lst]))
    print(lst2)

else:
    a=lst.pop()
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        lst2=list(''.join([str(i) for i in lst]))
    lst3=lst2.append(a)
    print(lst2)
