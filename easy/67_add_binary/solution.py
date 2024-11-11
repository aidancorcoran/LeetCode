# Problem
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# -------------------------------------------------------------------------------------------
# First Thoughts:
# Can add as string or convert to ints (this would use built in functions) and then return a string
# Potentially loop from the last index backwards if adding as a string

# We need to check each number backwards, if they are both 1's the result at that index is 0 and carry is 1
# Can build a string and then reverse it
# 111
#  11
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_index = len(a) - 1
        b_index = len(b) - 1
        carry = 0
        sum = []
        while a_index >= 0 or b_index >= 0 or carry:
            value = carry
            if a_index >= 0:
                value += int(a[a_index])
                a_index -= 1
            if b_index >= 0:
                value += int(b[b_index])
                b_index -= 1
            sum.append(str(value % 2))
            carry = value // 2
        return ''.join(sum[::-1])

                