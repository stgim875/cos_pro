# 17.2 continue로 실행 건너뛰기

# 1부터 100까지 중 짝수만 출력
for i in range(1, 101):         # 1부터 100까지 증가하면서 100번 반복
    if i % 2 != 0:                  # i를 2로 나누었을 때 나머지가 0이 아니면 홀수
        continue                    # 아래 코드를 실행하지 않고 건너 뜀
    print(i)

# 1부터 100까지 중 홀수만 출력
for i in range(1, 101):
    if i % 2 == 0:
        continue
    print(i)