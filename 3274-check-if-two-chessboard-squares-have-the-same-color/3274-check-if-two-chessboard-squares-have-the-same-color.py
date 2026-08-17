class Solution:
    def checkTwoChessboards(self, coordinate1, coordinate2):
        return (ord(coordinate1[0]) + int(coordinate1[1])) % 2 == \
               (ord(coordinate2[0]) + int(coordinate2[1])) % 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna