lst1=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lst2 = [lst1[i] for i in range(1,len(lst1))  if i  in range(1,len(lst1)) if lst1.count(lst1[i])==1]

print(f"Исходный список: {lst1}")
print(f"Новый список: {lst2}")
