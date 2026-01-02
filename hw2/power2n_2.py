# 方法 2a：用遞迴
n = 20
def power2n(n):
    if n == 0:
        return 1
    if n == 1: 
        return 2
    return power2n(n-1)+power2n(n-1)
print('方法二a', power2n(n)) 