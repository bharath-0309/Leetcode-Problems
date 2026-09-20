class Solution:
    def reverseDegree(self, s):
        ans = 0
        for i, c in enumerate(s, 1):
            ans += i * (26 - (ord(c) - ord('a')))
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna