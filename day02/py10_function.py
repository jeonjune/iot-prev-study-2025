# py10_function.py
# 함수 : 수학의 함수와 동일

print('함수!!') # 내장(built-in)함수

# 함수 정의(definition)
# 사용자 정의함수
def add(a, b) :
    result = a + b
    return result # return -> 결과를 돌려준다.(반환하다.)

def minus(a, b) :
    result = a - b
    return result

def multiple(a, b) :
    result = a * b
    print(result)
    return # 반환할 값이 없으면 리턴은 생략

def divide() :
    result = 100 / 4
    print('나누기 결과는', result)

x = 11
y = 22
z = add(x, y)
q = multiple(x, y)
# a = int(input('숫자를 입력하쇼 > '))
# b = int(input('숫자를 또 입력하쇼 > '))

print('합의 결과는', z)
# print('합의 결과는', add(a,b))
print('차의 결과는', minus(x,y))
# print('차의 결과는', minus(a,b))
print('곱의 결과는', q)
print('곱의 결과는?', multiple(10,30)) # print(result) 값이 먼저 출력되고 return 값이 출력되는데 아무것도 없어서 None 뜸
divide()

''' 내장함수 : 파이썬에서 자주 사용할 것 같은 함수를 미리 만들어둔 것 '''
# stdlib(standard library)에 들어있음
print('최대값은', max(1, 3, 7, 15))
print('최소값은', min(1, 3, 7, 15))
print('절대값은', abs(-5),'아오피곤해')
print(pow(2, 10) == 2 ** 10, 2 ** 10)
