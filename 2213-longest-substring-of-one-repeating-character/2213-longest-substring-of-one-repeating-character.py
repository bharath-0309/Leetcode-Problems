class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)

        def pull(node):
            l = node * 2
            r = l + 1

            left_char[node] = left_char[l]
            right_char[node] = right_char[r]

            pre[node] = pre[l]
            suf[node] = suf[r]
            best[node] = max(best[l], best[r])

            if right_char[l] == left_char[r]:
                best[node] = max(best[node], suf[l] + pre[r])

                if pre[l] == length[l]:
                    pre[node] += pre[r]

                if suf[r] == length[r]:
                    suf[node] += suf[l]

        length = [0] * (4 * n)

        def build(node, lo, hi):
            length[node] = hi - lo + 1

            if lo == hi:
                pre[node] = 1
                suf[node] = 1
                best[node] = 1
                left_char[node] = s[lo]
                right_char[node] = s[lo]
                return

            mid = (lo + hi) // 2
            build(node * 2, lo, mid)
            build(node * 2 + 1, mid + 1, hi)
            pull(node)

        def update(node, lo, hi, idx, ch):
            if lo == hi:
                left_char[node] = ch
                right_char[node] = ch
                pre[node] = 1
                suf[node] = 1
                best[node] = 1
                return

            mid = (lo + hi) // 2

            if idx <= mid:
                update(node * 2, lo, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, hi, idx, ch)

            pull(node)

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(best[1])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna