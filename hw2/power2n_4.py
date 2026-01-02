# 方法 3：用遞迴+查表
n = 20
m = [None]*10000
m[0] = 1
m[1] = 2

def power2n(n):
    if n < 0:
        raise
    if not m[n] is None: 
        return m[n]
    m[n] = power2n(n-1)+power2n(n-1) 
    return m[n]
print('方法三', power2n(n)) 