class IntToStrSolution:
    def isPalindrome(self, x: int) -> bool:
        str_value = str(x)
        
        if str_value == str_value[::-1]:
            return True
        return False