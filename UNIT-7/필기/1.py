# 2022년 2월 14일
# UNIT 문자열 사용하기

hello1 = 'Hello world!'
print(hello1)

hello2 = "Hello world!"
print(hello2)

hello3 = '안녕 하세요'
print(hello3)

hello = '''Hello, world!
안녕 하세요.
python입니다.'''
print(hello)

# 작은 따옴표와 큰따옴표를 사용하는 이유는 따옴표 안에 따옴표를 사용하려는 이유!
# print('Hello, "python"')
# print("Hello, 'python'")

# 큰따옴표 안에 큰따옴표를 사용할 수 없고, 작은따옴표 안에 작은따옴표를 사용할 수 없음
# print('Hello, 'python'')
# print("Hello, "python"")

# string_multiline_quote.py 실습 내용은 파일을 참고 바랍니다.

# 참고 : 문자열에 따옴표를 포함하는 방법
# 작은 따옴표 안에 작은따옴표를 넣을 수 없을까요? 방법이 있습니다. 다음과 같이 작은따옴표 앞에 \(역슬래시)를 붙이면됩니다.
print('Hello, \'python\'')
# 물론 큰따옴표도 동일하게 방식으로 붙이면됩니다.


year = 2022
month = 2
day = 14
hour = 16
minute = 45
second = 59

print(year, month, day, sep='/', end='')
