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
    def __init__(self, value) -> None:
        self.value = value
        self.children = []
    def addChild(self, child_node):
        self.children.append(child_node)
    def possibleWays(self):
        count = 0
        for child in self.children:
            if child.value == 0:
                count += 1
        return count
    def display(self, level=0):
        print("  " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)

class Solution:
    def climbStairs(self, n: int) -> int:
        rootStep = Tree(n)
        n_1 = n
        n_2 = n
        while n_1 and n_2 < 0:
            child_n_1 = Tree(n_1 - 1)
            child_n_2 = Tree(n_2 - 2)
            rootStep.addChild(child_n_1)
            rootStep.addChild(child_n_2)

            n_1 -= 1
            n_2 -= 2
        rootStep.display()
        return rootStep.possibleWays()
            