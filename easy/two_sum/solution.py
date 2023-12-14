class BruteForceSolution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        return []


class HashTableSolution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        number_map = {}
        n = len(nums)

        # Assign the nums as keys and their index as values (Hash map)
        for i in range(n):
            number_map[nums[i]] = i

        for i in range(n):
            complement = target - nums[i] # Getting the num that adds to make target

            if complement in number_map and number_map[complement] != i:
                return [i, number_map[complement]]
            
        return []

        