class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                cur = 0
                for i in range(n):
                    for j in range(n):
                        x = i + dr
                        y = j + dc
                        if 0 <= x < n and 0 <= y < n:
                            if img1[i][j] == 1 and img2[x][y] == 1:
                                cur += 1
                ans = max(ans, cur)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna