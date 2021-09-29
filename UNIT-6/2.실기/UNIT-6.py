# # 6-1 변수 만들기
# # 변수 만들기
x = 10
# x
print(x)


# # 6-2 빈 변수 만들기
# # 빈 변수 만들기
x = None
print(x)


# # 6-3 변수의 값 변경하기
x = 10
print(x)

y = 20
print(y)

c = 30+40
print(c)

# 6-4 변수 여러 개를 한 번에 만들기

x = y = z = 10, 20, 30
print(x)
print(y)
print(z)

# 만약 변수와 값의 개수가 맞지 않으면 다음과 같이 에러가 발생합니다.
# x, y, z = 10, 20
# print(x)
# print(y)
# print(z)

# 변수를 3개 넣어서 모두 같은 값을 할당
x = y = z = 10
print(x)
print(y)
print(z)

# 6-5 변수에 변수 할당하기

x = 10
y = x
print(x)

# 변수 여러 개에 변수를 각각 할당할 수도 있습니다.
a = 10
b = 20
x, y = a, b
print(a, b)

# 여러 개에 변수를 할당 할 때 자리를 바꿔주면 됩니다.
x = 10
y = 20
x, y = y, x
print(x)
print(y)

# 변수 삭제하기
# g = 10
# del g
# print(g)

# 6-6 퀴즈
# 문제 내용은 교재 참고 바람

# 6-7 연습문제: 변수 만들기
# 다음 소스코드를 완성하여 10, 10, 20, None이 각각 출력되게 만드세요.
k1 = k2 = 10
k3, k4 = 20, None
print(k1)
print(k2)
print(k3)
print(k4)
