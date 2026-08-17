class Solution:
    def digitFrequencyScore(self, n):
        freq = [0] * 10

        while n:
            freq[n % 10] += 1
            n //= 10

        return sum(d * freq[d] for d in range(10))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna