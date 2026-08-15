class Solution:
    def longestSubsequence(self, nums):
        xor = 0
        has_non_zero = False

        for num in nums:
            xor ^= num
            if num != 0:
                has_non_zero = True

        if xor != 0:
            return len(nums)

        if has_non_zero:
            return len(nums) - 1

        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna