# py08_star_print.py
# 별찍기

## 문자열에 사용할 수 있는 연산자는 +, * -> 추후 설명
'''
    *
   **
  ***
 ****
*****
'''
a = 5
for i in range(1, 6) :
    print(' ' * (a - i), end='')
    print('*' * i)

'''
*
**
***
****
*****           
'''
for i in range(1, 6) :
    print('*' * i)

    