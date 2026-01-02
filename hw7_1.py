def  matrixPrint(m):
    for i in range(len(m)):
        print(f'{m[i]}')

def strset(s,i,c):
    return s[:i] + c + s[i+1:]

def find(m, x, y): 
    print(f'=========================')
    print(f'x={x},y={y}')
    matrixPrint(m)

    if x >= len(m) or y >= len(m[0]) : #越界
        return False
    if m[x][y] == '-' or m[x][y] == '+': #碰壁&已走過
        return False
    if m[x][y] == ' ': #沒走過的
        m[x] = strset(m[x], y, '.') 
    if (x == 4 or y== 6): #走的位置
        return True
    
    if y<6 and m[x][y+1] ==' ': #右
        if find(m, x,y+1):
            return True
    if x<4 and m[x+1][y] ==' ': #下
        if find(m, x+1, y):
            return True
    if y>0 and m[x][y-1] ==' ': #左
        if find(m, x, y-1):
            return True
    if x>0 and m[x-1][y] ==' ': #上
        if find(m, x-1, y):
            return True
    m[x] = strset(m[x], y, '+')
    return False

m = ['--   --',
     '-  -  -',
     '  - - -',
     '- -   -',
     '--- -- '] 

find(m, 2, 0)

print(f'=========================')
matrixPrint(m)    
    
