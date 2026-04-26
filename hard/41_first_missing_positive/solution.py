
def solution( nums: list[int] ) -> int:
    smallest_num = 1 # this is the base case

    set_input = set(nums)

    while smallest_num in set_input:
        smallest_num += 1

    return smallest_num

def main():
    # So we have an array that is unsorted so we atleast need to check every element.
    # If we convert the array to a set that is linear time and then allows for fast lookups
    nums = [3,4,-1,1]

    print(solution(nums))

if __name__ == "__main__":
    main()