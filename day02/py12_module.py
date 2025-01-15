# py12_module.py
# 모듈

import py10_function as calc

print(calc.add(1, 2))

# 수학 함수를 편하게 모아둔 모듈
import math

result = math.pow(2,10)
print(result) # 실수로 출력
print(pow(2, 10)) # 정수로 출력

result = math.log(2)
print(result)
# print(log(2)) - 함수가 존재하지 않아서 모듈을 연결해줘야함

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests

import requests

res = requests.get('https://www.naver.com') # 네이버 사이트를 접속하라
print(res.status_code) # 200 : 웹사이트 접속
print(res.content)