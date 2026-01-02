def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    # 建立一個 (m+1) x (n+1) 的矩陣
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化邊界條件
    for i in range(m + 1):
        dp[i][0] = i  # 把 str1[0..i] 轉成空字串需要 i 次刪除
    for j in range(n + 1):
        dp[0][j] = j  # 把空字串轉成 str2[0..j] 需要 j 次插入
    
    # 動態規劃填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 字元相同，不需要操作
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # 刪除 (delete)
                    dp[i][j - 1],    # 插入 (insert)
                    dp[i - 1][j - 1] # 替換 (replace)
                )
    
    return dp[m][n]

# 範例測試
print(min_edit_distance("kitten", "sitting"))  # 輸出 3