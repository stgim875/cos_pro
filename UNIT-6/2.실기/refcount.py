# 참고
# 변수에 저장되는 방식

import sys
print(sys.getrefcount(1000))

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

print(x is y)
