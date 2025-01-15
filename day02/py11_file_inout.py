# py11_file_inout.py
# 파일입출력

# a(추가), r(읽기), w(쓰기)
f = open('./day02/textfile.txt', mode='w', encoding='UTF-8')
# 아무것도 안함
f.write('발목이 욱씬거려용.\n')
f.write('집가고싶다.\n')
f.close()

print('텍스트파일이 생성되었습니다.')

## 읽기
f = open('./day02/textfile.txt', mode='r', encoding='UTF-8')

while True : # 무한반복
    line = f.readline() # 한 줄씩 읽고
    if not line : break # 읽을 줄이 없으면 반복문 탈출
    
    print(line)
    
f.close()