from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start_ptr = 0
        end_ptr = len(nums) - 1

        while start_ptr <= end_ptr:
            if nums[start_ptr] == val:
                # Simple Case 1: The element is bad.
                # Replace it and shrink the boundary.
                # DON'T advance start_ptr. Let the next loop re-check.
                nums[start_ptr] = nums[end_ptr]
                end_ptr -= 1
            else:
                # Simple Case 2: The element is good.
                # Keep it and move on.
                start_ptr += 1
                
        # The loop condition naturally handles all cases.
        # `start_ptr` is our answer. No extra variable needed.
        return start_ptr