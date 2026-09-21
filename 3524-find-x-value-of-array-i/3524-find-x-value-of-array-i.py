class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            ndp = [0] * k
            ndp[x] = 1

            for r in range(k):
                ndp[(r * x) % k] += dp[r]

            for r in range(k):
                ans[r] += ndp[r]

            dp = ndp

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna