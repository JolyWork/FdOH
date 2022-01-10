try:
    K = 3
    s=open("text.txt","r")
    s1=s.read()
    s.close()

    print(s1)
    s2 = list(map(str, s1.split()))
    print(s2)

    res = []
    for i in s2:
        if len(i) == K:
            res.append(i)
    print(res)

    s=open("textres.txt","w")
    for i in res:
        s.write(str(i) + ' ')
    s.close()

except  FileNotFoundError:
    print('Файл не найден')
except  TypeError:
    print('Несоответсвующий тип')
except:
    print('Возникла ошибка')    
