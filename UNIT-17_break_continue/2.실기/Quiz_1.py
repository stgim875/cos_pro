# 143p

# 17.5 퀴즈

# 2. 다음 코드로 1부터 10까지 출력하면서 3의 배수는 제외 하려고 할 때 밑줄 부분에 들어가야 할 코드를 고르세요.

# 3 일 경우 반복 중단 코드
for i in range(1, 100):
    if i % 3 == 0:
        break
    print(i)

# 3의 배수 제외 코드
for i in range(1, 11):
    if i % 3 ==0:
        continue
    print(i)

# 반복 중단
for i in range(1, 11):
    if i % 3 != 0:  
        break
    print(i)

# 3의 배수 코드
for i in range(1, 11):
    if i % 3 != 0:
        continue
    print(i)

# 3의 배수 코드
for i in range(1, 11):
    if i % 3 == 0:
        print(i)

# 3. 다음 코드로 30부터 10까지 출력 할 때 밑줄 부분에 들어가야 할 코드를 고르세요.

# a번 : 30 출력되고 반복 종료
i = 30

while True:
    print(i)
    if i != 10:
        break
    i -= 1

# b번 : 30 무한 반복
i = 30

while True:
    print(i)
    if i != 10:
        continue
    i -= 1

# c번 : 30부터 10까지 출력
i = 30

while True:
    print(i)
    if i == 10:
        break
    i -= 1

# d번 : 10 무한 반복
i = 30

while True:
    print(i)
    if i == 10:
        continue
    i -= 1

#  e번 : 30 무한 반복
i = 30
while True:
    print(i)
    if i <=30:
        continue