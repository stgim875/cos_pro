# 16-4 입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요 : '))

while count > 0:   # count가 0 보다 클 때 반복
    print('Hello, world! %d' ,   count) 
    count -= 1    # count를 1씩 감소시킴
