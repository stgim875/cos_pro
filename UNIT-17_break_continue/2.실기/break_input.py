# 17.3 입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요 : '))

i = 1
while True:
    print(i)
    if i == count:
        break
    i += 1

########################################

# range() 사용하여 반복 횟수 지정하기

i = 1
while range(0, 100): 
    print(i)
    if i == count:
        break
    i += 1