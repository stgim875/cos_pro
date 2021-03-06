# 5-1 정수 계산하기(39p ~ 40p)

print(1+1)  # 2
print(1-2)  # -1
print(2*2)  # 4
print(5/2)  # 2.5
print(2/5)  # 2.5

# 정수 나눗셈의 결과를 정수로 만들고 싶을 때는 int를 붙여준다.
print(int(5/2))  # 2

# 2진수, 8진수, 16진수
print(0b110)  # 6 출력
print(0o10)  # 8 출력
print(0xf)  # 15 출력

# 5-2 실수 계산히기(41p ~ 42p)

print(3.5+2.1)
print(4.3-2.7)
print(5.5 / 3.1)

# 정수를 실수로 만들기
print(float(1+2))

# 복소수
print(complex(1.2, 1.3))

# 5-3 스크립트 파일에서 계산하기

# 문제 풀기
# 다음중 10/4를 계산한 결과로 올바른 것을 고르세요.
print(10/4)

# sub.py 파일에서 19-5의 결과를 출력하려고 합니다. 올바른 것을 고르세요.
print(19-5)

# 연습문제
# 게임에서 '왜곡'이라는 스킬이 225+0.6(Ability power, 주문력)의 피해를 입힙니다.(주문력 : 102)
print(225+(0.6*102))

a = 225
b = 0.6
c = 102
print(a+(b*c))
