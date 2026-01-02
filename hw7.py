objs = ["人", "狼", "羊", "菜"]
state = [0, 0, 0, 0]

def neighbors(s): 
    side = s[0]
    next = []
    add(next, move(s, 0))
    for i in range(1, len(s)):
        if(s[i] == side):
            add(next, move(s,i))
    return next

def add(next, s): #確定移動
    if not isDead(s):
        next.append(s)

def move(s, obj): #移動到對面
    nS = s.copy()
    side = s[0]
    anotherSide = 1 if side == 0 else 0
    nS[0] = anotherSide
    nS[obj] = anotherSide
    return nS

visitedMap = {}

def visited(s):
    visit = ''.join(map(str, s))
    return visit in visitedMap

def isDead(s): #失敗
    if(s[1] == s[2] and s[1] != s[0]):
        return True
    if(s[2] == s[3] and s[2] != s[0]):
        return True
    return False
    
def isSuccess(s): #成功
    return all(x == 1 for x in s)

path = []

def dfs(s): #深度優先
    if(visited(s)):
        return
    path.append(s)
    if(isSuccess(s)):
        printPath(path)
        return
    visitedMap[''.join(map(str, s))] = True
    neighborsList = neighbors(s)
    for ns in neighborsList:
        dfs(ns)
    path.pop()

def chstr(s):
    result = ''
    for i in range(len(s)):
        side = "左" if s[i] == 0 else "右"
        result += objs[i] + side + " "
    return result

def printPath(path):
    for i in range(len(path)):
        print(chstr(path[i]))

dfs(state)

