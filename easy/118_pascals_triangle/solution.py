class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        soln = []
        default_num = 1

        for i in range(numRows):
            print(f"i: {i}")
            for x in range(i):
                print(f"x: {x}")

        return
        # Loop over the num rows
        # If the soln array does havent a num at the previous value and previous - 1 then it is 1
        # if it does then the number is the sum of the two previous
        # if previous 



if __name__ == "__main__":
    soln = Solution()

    soln.generate(5)