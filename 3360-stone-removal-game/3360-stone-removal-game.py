class Solution:
    def canAliceWin(self, n):
        remove = 10
        turn = 0

        while n >= remove:
            n -= remove
            remove -= 1
            turn += 1

        return turn % 2 == 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna