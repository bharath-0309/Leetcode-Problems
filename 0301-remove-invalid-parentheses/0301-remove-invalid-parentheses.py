from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if not s:
            return [""]

        queue = deque([s])
        visited = set([s])
        res = []
        found = False

        while queue:
            curr = queue.popleft()
            
            if isValid(curr):
                res.append(curr)
                found = True
            
            # If we found a valid string at the current depth, 
            # we don't need to explore further depths (minimum removals)
            if found:
                continue
            
            for i in range(len(curr)):
                if curr[i] not in ('(', ')'):
                    continue
                
                # Generate new string by removing the character at index i
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
                    
        return res