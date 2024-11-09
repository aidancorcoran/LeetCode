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
# Can add as string or convert to ints and then return a string
# Potentially loop from the last index backwards if adding as a string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, base=2)
        b_int = int(b, base=2)

        return(bin(a_int+b_int)[2:])