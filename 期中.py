from collections import deque

#迷宮版型
m = [
    ['1', '1', '1', '1', '1', '1'],
    ['1', ' ', ' ', 'o', ' ', '1'],
    ['1', ' ', '1', '1', 'o', '1'],
    ['1', ' ', ' ', ' ', ' ', '1'],
    ['1', 'o', '1', ' ', ' ', '1'],
    ['1', '1', '1', ' ', '1', '1']
]

rows = len(m)
cols = len(m[0])

pl_dir= (1, 1)
mon_dir = (5, 3)

beans = [(1, 3), (2, 4), (4, 1)]
eaten = set()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右


def print_maze(): #印迷宮
    print('============')
    print(f'P{pl_dir}')
    print(f'M{mon_dir}')
    for r in range(rows):
        for c in range(cols):
            if (r, c) == pl_dir:
                print('P', end=' ')
            elif (r, c) == mon_dir:
                print('M', end=' ')
            elif (r, c) in beans:
                print('o', end=' ')
            elif (r, c) in eaten:
                print('.', end=' ')
            else:
                print(m[r][c], end=' ')
        print()

def bfs(start, goal): #廣度優先
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]
        for d in directions:
            new_dir = (current[0] + d[0], current[1] + d[1])
            if (0 <= new_dir[0] < rows and 0 <= new_dir[1] < cols and
                m[new_dir[0]][new_dir[1]] != '1' and new_dir not in visited): #檢查
                queue.append((new_dir, path + [current]))
                visited.add(new_dir)
    return None

def best_distance(src, beans): #到豆子最短路徑
    best = None
    best_len = float('inf')
    for b in beans:
        path = bfs(src, b)
        if path and len(path) < best_len:
            best = b
            best_len = len(path)
    return best

def move_pl(): #玩家移動
    global pl_dir, beans
    if beans:
        target = best_distance(pl_dir, beans)
        if target:
            path = bfs(pl_dir, target)
            if path and len(path) > 1:
                pl_dir = path[1]

def move_mon(): #怪物移動
    global mon_dir
    best_move = None
    best_distance = float('inf')
    for d in directions:
        new_dir = (mon_dir[0] + d[0], mon_dir[1] + d[1])
        if 0 <= new_dir[0] < rows and 0 <= new_dir[1] < cols and m[new_dir[0]][new_dir[1]] != '1':
            distance = abs(new_dir[0] - pl_dir[0]) + abs(new_dir[1] - pl_dir[1])
            if distance < best_distance:
                best_move = new_dir
                best_distance = distance
    if best_move:
        mon_dir = best_move

def game(): #遊戲
    global pl_dir, mon_dir, beans, eaten
    round = 0
    while True:
        print_maze()
        prev_pl_dir = pl_dir
        move_pl()
        move_mon()
        if pl_dir in beans:
            beans.remove(pl_dir)
            eaten.add(pl_dir)
        if not beans:
            print_maze()
            print('Win!')
            break
        if pl_dir == mon_dir or mon_dir == prev_pl_dir:
            print('Game Over!')
            break
        round += 1

game()  

