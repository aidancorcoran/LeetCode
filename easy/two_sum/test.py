from solution import BruteForceSolution, HashTableSolution
import time
import random

nums = []
target = 9

for i in range(1000):
    nums.append(random.randint(1,1000))


brute = BruteForceSolution()

start = time.process_time()
brute_force_solution = brute.twoSum(nums, target)
time_taken = time.process_time() - start
print("The brute force solution: ", brute_force_solution, "Time: ", time_taken, "s")


hash = HashTableSolution()

start = time.process_time()
hash_table_solution = hash.twoSum(nums, target)
time_taken = time.process_time() - start
print("The hash table solution: ", hash_table_solution, "Time: ", time_taken, "s")

