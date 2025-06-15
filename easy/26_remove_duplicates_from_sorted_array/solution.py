# Problem 26. Remove Dupliace items from sorted array

from typing import List


class Solution():
    def removeDuplicates(self, nums: List[int]) -> int:
        # We have an int array in ascending order
        # For each unique element we push it to the new array
        # Then increase dup_count if the next num == the previous

        if not nums:
            return 0
        
        k = 1 # Next good index, first element 0 is always uniqu

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
            
        return k


        