class Solution:
    def isGoodArray(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = 0

        for num in nums:
            g = gcd(g, num)

            if g == 1:
                return True

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna