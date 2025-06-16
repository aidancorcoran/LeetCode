from solution import Solution

solution_obg = Solution()

nums = [0,1,2,2,3,0,4,2]

print(nums)

elements_to_keep = solution_obg.removeElement(nums=nums, val=2)

print(nums, elements_to_keep)