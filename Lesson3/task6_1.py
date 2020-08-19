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
        
        
        
print(int_func(input(f"Введите слово из маленьких латинских букв: ")))
