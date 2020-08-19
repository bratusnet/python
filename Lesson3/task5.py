def my_func(*args):
    s=0
    st=0
    while st==0:  
        x=input("Введите строку чисел, разделенных пробелом или q для выхода: ")
        y=x.split() 
        for i in range(len(y)):
            
            if  y[i-1] =='q':
                st=1
                                
            else:
                s=s+int(y[i-1])
                
        print (f"Полученная сумма: {s}")
    
print(my_func())


