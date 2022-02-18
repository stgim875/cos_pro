# 16.1 while 반복문 사용하기
# 100번 출력하기
i = 0
while i < 100:
    print('Hello, world!')
    i += 1

# 16-2 초깃값을 1부터 시작하기
# i를 입력하여 100번 출력하기
i = 0
while i < 100:
    print('Hello, world!', i)
    i += 1

# 16-3 초깃값을 감소시키기
# i를 100부터 1까지 100번 출력하기
i = 100
while i > 0:
    print('Hello, world!' , i)
    i -= 1

# 16-6 while 반복문으로 무한 루프 만들기

    # while 1:  # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
    # print('Hello, world!')

# while 'Hello':
#     print('Hello, world!') #  내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
