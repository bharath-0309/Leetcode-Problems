class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        current = 0
        ans = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left += 1

            seen.add(nums[right])
            current += nums[right]

            ans = max(ans, current)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna