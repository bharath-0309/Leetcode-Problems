class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        left_len = [0] * (4 * n)
        right_len = [0] * (4 * n)
        best = [0] * (4 * n)
        length = [0] * (4 * n)

        def build(node, l, r):
            length[node] = r - l + 1

            if l == r:
                left_char[node] = right_char[node] = s[l]
                left_len[node] = right_len[node] = best[node] = 1
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node)

        def merge(node):
            L = node * 2
            R = node * 2 + 1

            left_char[node] = left_char[L]
            right_char[node] = right_char[R]

            left_len[node] = left_len[L]
            if left_len[L] == length[L] and right_char[L] == left_char[R]:
                left_len[node] += left_len[R]

            right_len[node] = right_len[R]
            if right_len[R] == length[R] and right_char[L] == left_char[R]:
                right_len[node] += right_len[L]

            best[node] = max(best[L], best[R])

            if right_char[L] == left_char[R]:
                best[node] = max(
                    best[node],
                    right_len[L] + left_len[R]
                )

        def update(node, l, r, idx, char):
            if l == r:
                left_char[node] = right_char[node] = char
                left_len[node] = right_len[node] = best[node] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(best[1])

        return ans