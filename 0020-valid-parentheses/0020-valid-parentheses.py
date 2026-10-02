class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop the top element if stack is not empty, else assign a dummy character
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the top element, return False
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)

        # If stack is empty, all brackets were matched correctly
        return not stack