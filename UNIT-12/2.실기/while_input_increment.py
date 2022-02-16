# 16-4  입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요 : '))

i = 0
while i < count:   # i가 count 보다 작을 때 반복
    print('Hello, wold! %d' % i)
    i += 1