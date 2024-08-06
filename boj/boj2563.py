# 색종이, 실버5

tc = int(input())
arr = [[0] * 100 for i in range(100)]
for _ in range(tc):
    x, y = map(int, input().split())
    for i in range(x, x+10): 
        for j in range(y, y+10):
            arr[i][j] = 1
    
result = 0
for i in range(100):
    result += sum(arr[i])

print(result)