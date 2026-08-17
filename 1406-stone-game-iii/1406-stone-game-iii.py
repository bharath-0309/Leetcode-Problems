class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            total = 0
            dp[i] = float("-inf")

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                dp[i] = max(dp[i], total - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna