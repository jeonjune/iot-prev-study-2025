# py05_if_control.py
# if문

## int(정수화), float(실수화), double(복소수화)
age = int(input('나이를 입력하시오. > ')) # age 문자열이 입력 30 -> '30'

print(str(age)+'0','짤')

## if문이 시작하겠다는 것을 의미하는 마지막 단어 -> :
if age > 19 :
    # if문이 참(True)이면 이 아래의 구문을 실행
    # if문(흐름제어) 안으로 들어왔다!
    print(age, '짤은 술담배 구매 가능합니다.')
elif age == 19 :
    # 다른 조건이 필요할 때 (else if) - 여러번 사용 가능
    print('내년에 와라')
else :
    # if문이 거짓(False)이면, 아래 구문 실행
    print('꺼져')