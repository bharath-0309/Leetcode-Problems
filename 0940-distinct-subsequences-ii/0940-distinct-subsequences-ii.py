class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007
        dp = [0] * 26

        for c in s:
            i = ord(c) - 97
            dp[i] = (sum(dp) + 1) % MOD

        return sum(dp) % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna