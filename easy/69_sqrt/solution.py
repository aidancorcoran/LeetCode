class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        init_guess = x / 2
        for i in range(10):
            next_guess = (1/2)*(init_guess + (x/init_guess))
            init_guess = next_guess

        return next_guess.__floor__()


4



if __name__ == "__main__":
    soln = Solution()

    print(soln.mySqrt(64))