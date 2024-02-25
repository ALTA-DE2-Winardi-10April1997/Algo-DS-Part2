def maximum_buy_product(money, product_price):
    n = len(product_price)
    dp = [[0]*(money+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(money+1):
            if product_price[i-1]<=j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - product_price[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

     
    return dp[n][money]

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0