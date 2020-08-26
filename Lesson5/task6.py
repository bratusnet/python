sub = {}
with open('file_task6.txt', 'r', encoding="utf-8") as fil:
    for line in fil:
        subject=line.split()[0]
        
        if line.split()[1]=='-':
            lec=0 
        else:
            lec=line.split()[1].split('(')[0]
        
        if line.split()[2]=='-':
            pra=0 
        else:
            pra=line.split()[2].split('(')[0]

        if line.split()[3]=='-':
            lab=0 
        else:
            lab=line.split()[3].split('(')[0]       

        sub[subject] = int(lec) + int(pra) + int(lab)
    print(f'Сформированный словарь - \n {sub}')
