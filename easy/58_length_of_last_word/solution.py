# Problem
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


# Thought process:
# A string with words and spaces, lets split it up into individual array elements
# based off of space characters and determine the last element using len()


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_array = s.split()
        
        if not len(string_array):  # Check if the length of the array is 0, if it is return 0
            return 0
        
        # We want to return the length of the final word in the string array, which is len(array) -1
        return len(string_array[len(string_array) - 1])  