import bisect

# Precompute all binary palindromes up to a safe upper limit
P = []
for i in range(1, 10001):
    s = bin(i)[2:]
    if s == s[::-1]:
        P.append(i)

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in nums:
            idx = bisect.bisect_left(P, x)
            
            # Find the minimum distance to either the exact match, 
            # the immediate larger binary palindrome, or the immediate smaller one.
            min_ops = float('inf')
            
            if idx < len(P):
                min_ops = min(min_ops, abs(P[idx] - x))
            if idx > 0:
                min_ops = min(min_ops, abs(P[idx - 1] - x))
                
            ans.append(min_ops)
            
        return ans