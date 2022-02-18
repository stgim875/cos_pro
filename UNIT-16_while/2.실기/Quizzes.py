# 16.7 퀴즈

# i = 10

# while i < 19:
#     print(i, end=' ')
#     i += 2

i = 0
while i > 20:  # i 값이 작을 때 무한 반복인데 현재 i 값이 20보다 크다로 되어 있어서 거짓
    print('Hello, world!')
    i = i + 2

i = 0
while i < 20:  # i 값이 작을 때 무한 반복인데 현재 i 값이 20보다 크다로 되어 있어서 거짓
    print('Hello, world!', i)
    i = i + 2

# 16.8 퀴즈
# 다음 소스 코드를 완성하여 정수 2 5, 4 4, 8 3, 16 2, 32 1이 각각 출력되게 만드세요.

i = 2
j = 5

while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1