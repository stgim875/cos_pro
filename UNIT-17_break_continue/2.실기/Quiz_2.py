# 144p

# 17.6 연습문제
#다음 소스 코드를 완성하여 1과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력되게 만드세요.

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end= ' ')
    i += 1