class Solution:
    def stoneGameV(self, a):
        n = len(a)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + a[i]

        dp = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        for i in range(n):
            left[i][i] = a[i]
            right[i][i] = a[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = pre[j + 1] - pre[i]

                lo, hi = i, j - 1

                while lo <= hi:
                    k = (lo + hi) // 2
                    s = pre[k + 1] - pre[i]

                    if s * 2 < total:
                        lo = k + 1
                    else:
                        hi = k - 1

                k = lo

                if k > i:
                    dp[i][j] = max(dp[i][j], left[i][k - 1])

                if k < j:
                    dp[i][j] = max(dp[i][j], right[k + 1][j])

                if k <= j - 1:
                    s = pre[k + 1] - pre[i]
                    if s * 2 == total:
                        dp[i][j] = max(
                            dp[i][j],
                            s + dp[i][k],
                            s + dp[k + 1][j]
                        )

                left[i][j] = max(
                    left[i][j - 1],
                    dp[i][j] + total
                )

                right[i][j] = max(
                    right[i + 1][j],
                    dp[i][j] + total
                )

        return dp[0][n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna