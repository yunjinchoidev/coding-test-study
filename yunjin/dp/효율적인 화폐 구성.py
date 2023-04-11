N, M = map(int, input().split())
moneys = [int(input()) for i in range(N)]
moneys.sort(reverse=True)  # 큰 화폐단위 부터 체크하기 위함.

# 최초에 -1 로 초기화
dp = [-1 for i in range(100001)]  #

# 주어진 화폐 단위는 1개로 만들 수 있음.
for money in moneys:
    dp[money] = 1

# 주어진 화폐 다음 값부터 확인한다.
for i in range(max(moneys) + 1, M + 1):
    x = float('inf')

    # 모든 화폐 단위에 대해서 최솟값을 찾는다.
    for money in moneys:  # 큰 화폐 단위부터 확인해서
        if dp[i - money] != -1:  # 화폐 단위 하나만 추가할 수 있다면
            x = min(x, dp[i - money])  # 대소비교를 해준다

    if x != float('inf'):  # 값이 갱신 되었다면
        dp[i] = x + 1  # 갱신된 값에 1을 더해준다.
    else:
        dp[i] = -1  # 여전히 무한대라면 만들 수 없는 값이므로 -1

print(dp[M])
