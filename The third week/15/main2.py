def solve():
    n = int(input())
    home = input().strip()[:n]
    s, t = map(int, input().split())

    left = min(s, t) - 1
    right = max(s, t) - 1

    segment = home[left:right+1]

    ans = 0
    cnt = 0
    for ch in segment:
        if ch == 'H':
            cnt += 1          
        else:
            if cnt > 0:       
                ans += bin(cnt).count('1')   
                cnt = 0
    
    if cnt > 0:
        ans += bin(cnt).count('1')

    print(ans)
    
solve()