class Solution:
    def numDistinct(self, s, t):
        dp = [1] + [0] * len(t)

        for c in s:
            for j in range(len(t), 0, -1):
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna