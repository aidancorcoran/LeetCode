class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        output_string = ""

        # Sort the strings as this will ensure they are in proper order
        sorted_array = sorted(strs) 
        
        # First and last word must match
        first_word = sorted_array[0]
        last_word = sorted_array[-1]

        for i in range(min(len(first_word),len(last_word))):
            if first_word[i] != last_word[i]:
                return output_string
            output_string += first_word[i]
            
        return output_string