# 16-5 반복횟수가 정해지지 않은 경우

import random

i = 0
while i != 3:  # 3이 아닐 때 계속 반복
    i = random.randint(0, 9)
    print(i)