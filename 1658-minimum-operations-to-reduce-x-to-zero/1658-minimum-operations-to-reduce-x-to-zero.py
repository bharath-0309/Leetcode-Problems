class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x
        left = 0
        total = 0
        best = -1

        for right in range(len(nums)):
            total += nums[right]

            while total > target and left <= right:
                total -= nums[left]
                left += 1

            if total == target:
                best = max(best, right - left + 1)

        if target == 0:
            return len(nums)

        return -1 if best == -1 else len(nums) - best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna