class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        duplicate_count = 0
        uniqueList = []

        for i in range(len(nums)):
            if nums[i] not in uniqueList:
                uniqueList.append(nums[i])
            elif nums[i] in uniqueList:
                duplicate_count += 1
        
        for i in range(len(nums)):
            if i < len(uniqueList):
                nums[i] = uniqueList[i]
            else:
                nums[i] = 0
        
        return nums