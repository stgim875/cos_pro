# 17.1 break로 반복문 끝내기

i = 0
while True:              # 무한 루프
    i += 1                 # i를 1씩 증가시킴
    print(i)
    if i == 100:        # i가 100일 때 
        break            # 반복문을 끝냄. while의 제어 흐름을 벗어남

# i = i + 1 로 사용할 경우
i = 0
while True:
    print('Hello, world!', i)
    i = i + 1
    if i ==100:
        break

# i+= 1로 사용할 경우
i = 0
while True:
    print('Hello, world!', i)
    i += 1
    if i ==100:
        break