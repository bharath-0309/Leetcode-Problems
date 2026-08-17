class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                left_sum = pre[r + 1] - pre[l + 1]
                right_sum = pre[r] - pre[l]

                dp[l][r] = max(
                    left_sum - dp[l + 1][r],
                    right_sum - dp[l][r - 1]
                )

        return dp[0][n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna