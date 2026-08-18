import heapq

class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            effort, r, c = heapq.heappop(pq)

            if r == m - 1 and c == n - 1:
                return effort

            if effort > dist[r][c]:
                continue

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = max(
                        effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))

        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna