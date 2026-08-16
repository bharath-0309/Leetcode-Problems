class Solution:
    def predictTheWinner(self, nums):
        dp = nums[:]

        for length in range(2, len(nums) + 1):
            for i in range(len(nums) - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i + 1],
                            nums[j] - dp[i])

        return dp[0] >= 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna