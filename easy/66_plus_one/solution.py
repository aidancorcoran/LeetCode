# Problem ---------
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
 
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
# ------------------------------------------------------------------

# Initial thoughts:
# Check to ensure the last digit is not 9, if it is we can recursively call the
# function to ensure the number isn't 99999 for example

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        loop_of_nines=0
        if digits[index] == 9:
            loop_of_nines = 1

        while loop_of_nines:  # Loop from the last element backwards incase number is 9999 for example
            if digits[index] == 9:
                digits[index] = 0
                index -= 1
                if index == -1:
                    digits.insert(0, 1)
                    return digits
            if digits[index] != 9:
                 loop_of_nines = 0
        
        digits[index] = digits[index] + 1  # Increment the last digit by one and assign to itself
        
        return digits
