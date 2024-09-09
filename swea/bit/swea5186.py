import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = str('')
    for i in range(13):
        N = N * 2
        if N >= 1:
            if N == 1:
                result += '1'
                break
            result += '1'
            N -= 1
        else:
             result += '0'
    
    if i != 12:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} overflow')
            
        
             
