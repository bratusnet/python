def ext_func(arg_2):
    a=arg_2.split()
    ls=[]
    for i in range(len(a)):
        arg_1=a[i]
        def int_func(arg_1):
                l=list(arg_1)
                l2=[]
                for i in range(len(l)):
                    if ( ord(l[i-1])<97 or ord(l[i-1])>122):
                        print("Введен недопустимый символ")
                        l2=''
                        break
                    else:
                        l2.append(l[i])
                l3=''.join(l2).title() 
                return l3
        ls.append(int_func(arg_1))
    res=' '.join(ls)       
    return res
               
print(ext_func(input(f"Введите несколько слово из маленьких латинских букв через пробел: ")))
