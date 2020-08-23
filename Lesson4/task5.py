from functools import reduce

l=[range(100,1001)[i] for i in range(len(range(100,1001))) if range(100,1001)[i]%2==0]
print(f"Полученный список: {l} \n")

print(f"Результат через reduce: {reduce(lambda x, y: x*y, l)}\n")

def multiply(lst):
    answer = 1
    for i in lst:
        answer *= i
    return answer
 
print(f"Результат через функцию: {multiply(l)}")
