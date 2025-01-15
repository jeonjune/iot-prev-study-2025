# py06_for_control.py
# for문 - 프로그래밍의 꽃!

# range(9) => 0,1,2,3,4,5,6,7,8
# print(range(9))

for i in range(9) :
    # for문(흐름제어) 안으로 들어왔다!
    print(str(i)+'1',end='\t') # \t 가로 정렬

# 1부터 10까지의 합
sum = 0
for i in range(1, 101) :
    sum = sum + (i)
print('\n') # \n 한줄 내림
print(sum)

sum = 0
for i in range(1, 10, 2) :
    print(i)

 