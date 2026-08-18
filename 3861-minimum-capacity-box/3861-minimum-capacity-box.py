class Solution:
    def minimumIndex(self, capacity, itemSize):
        ans = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if ans == -1 or capacity[i] < capacity[ans]:
                    ans = i

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna