# py09_gugudan.py
# 구구단 프로그램

for i in range(2, 10) :
    print(str(i)+'단')
    if i == 9 :
        break
    for j in range(1, 10) :
        if j == 9 :
            break
        # print(str(i)+' * '+str(j)+' = ',end='')
        # print(i * j)
        print(i, '*', j, '=', i*j,end='\t')

    print()    