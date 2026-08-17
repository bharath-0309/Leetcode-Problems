class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        dp = piles[:]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                dp[l] = max(
                    piles[l] - dp[l + 1],
                    piles[r] - dp[l]
                )

        return dp[0] > 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna