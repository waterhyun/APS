# 알파벳 찾기

string = list(input())
arr = [-1] * (ord('z') - ord('a') + 1)
for i in range(len(string)):
    if arr[ord(string[i]) - 97] == -1:
        arr[ord(string[i]) - 97] = i
print(*arr)