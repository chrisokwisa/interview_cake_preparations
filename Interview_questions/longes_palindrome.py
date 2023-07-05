# A paplinrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.

# Example: 
# Input: "banana"

# Output: "anana"

class solution:
    def longestPalindrome(self, s):

        longest_palindrome = ""
        
        for i in range(len(s)):
            for j in range(i, (len(s))):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring

        return longest_palindrome
    

# Test Program

s = "tracecars"
print(str(solution().longestPalindrome(s))) 
# str is used to convert the output to a string and 
# solution() is used to call the function

# racecar