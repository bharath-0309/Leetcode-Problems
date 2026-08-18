class Solution:
    def maxPoints(self, technique1, technique2, k):
        n = len(technique1)
        diff = []

        for i in range(n):
            diff.append(technique1[i] - technique2[i])

        diff.sort(reverse=True)

        ans = sum(technique2)

        for i in range(k):
            ans += diff[i]

        for i in range(k, n):
            if diff[i] > 0:
                ans += diff[i]

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna