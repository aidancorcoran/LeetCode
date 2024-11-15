# Problem
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# ---------------------------------------------------------------------------------------
# First thoughts:
# To reach the nth step your previous step could by (n-2) or (n-1)
#              n
        #    n-1   n-2
        # n-1  n-2  n-1 n-2
# Seems like you can break it down to a binary tree

# n = 3
#               3
        #     2      1
        #  1    0  1   nul
class Tree:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.data = None


class Solution:
    def climbStairs(self, n: int) -> int:
        