# 17.4 입력한 숫자까지 짝수 출력하기

count = int(input('반복할 횟수를 입력하세요 : '))

for i in range(1 , count + 1):        # 1부터 증가하면서 count까지 반복(count+1)
    if i % 2 != 0:                          # i를 1로 나누었을 때 나머지가 0이 아니면 홀수
        continue                            # 아래 코드를 실행하지 않고 건너뜀
    print(i)