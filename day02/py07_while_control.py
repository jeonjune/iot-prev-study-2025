# py07_while_control.py
# while문

loop = 10
while loop >= 0 : # loop 변수값이 0보다 큰 동안 반복
    print(loop, end='\t')
    loop = loop - 1

print()

for i in range (10, -1, -1):
    print(i, end='\t')

print()

# 무한반복
num = 0
while True :
    print('Hello', num)
    num = num + 1