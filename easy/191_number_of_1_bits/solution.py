class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryNum = bin(n)
        # Split the string to remove the 0b from the front of bin str
        splitStr = binaryNum.split('b')
        return splitStr[1].count('1')