from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: # Empty list
            return None

        left = 0 
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return left