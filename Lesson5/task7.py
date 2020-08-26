import json
final_list=[]
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_task7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, revenue, loss = line.split()
        profit[name] = int(revenue) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'no Average profit')
    pr = {'Average profit': round(prof_aver)}
    print(f'Profit by company : {profit}')
    final_list.append(profit)
    final_list.append(pr)
    print(f'Финальный список : {final_list}')

with open('file_7.json', 'w', encoding="utf-8") as js:
    json.dump(final_list, js)
    js1 = json.dumps(final_list)
    print(f'Содержимое json-объекта : \n  {js1}')
