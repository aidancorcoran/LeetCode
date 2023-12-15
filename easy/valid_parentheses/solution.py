class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for bracket in s:
            if bracket in hash_map: # Opening bracket
                stack.append(bracket)
            else:
                if len(stack) == 0 or bracket != hash_map[stack.pop()]:
                    return False
                
        return len(stack) == 0