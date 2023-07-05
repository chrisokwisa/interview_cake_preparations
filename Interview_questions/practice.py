# def fizzbuzz():
#     """
#     Write a program that prints the numbers from 1 to 100.
#     But for multiples of three print “Fizz” instead of the number
#     and for the multiples of five print “Buzz”.
#     For numbers which are multiples of both three and five print “FizzBuzz”.
#     """
#     for m in range(1, 101):
#         if m % 3 == 0 and m % 5 == 0:
#             print("FizzBuzz ", end="")
#         elif m % 3 == 0:
#             print("Fizz ", end="")
#         elif m % 5 == 0:
#             print("Buzz ", end="")
#         else:
#             # print("{} ".format(m), end="")
#             print(m, end=" ")  # same as above

# # test
# fizzbuzz()



# def find_max(nums):
#     max_num=float("-inf") # smaller than all the other numbers
#     for num in nums:
#         if num > max_num:
#             # Fill in the missing line here
#             max_num = num
#             # 
#     return max_num


#  A palindrome is a sequence of characters that reads the same backwards and forwards.
#  Given a string, s, find the longest palindromic substring in s.

#  Example:
#  Input: "banana"
#  Output: "anana"

#  Input: "million"
#  Output: "illi"

class solution:
    def longestPalindrome(self, s):
        """ 
        :type s: str
        :rtype: str

        """

        # solution 1
        # brute force approach 

        # brue force approach is to check every substring of the string and see if it is a palindrome and 
        # if it is a palindrome then check if it is longer than the current longest palindrome substring
         


        # O(n^3) time complexity because of the nested for loops that are each O(n) they are nested 3 times so O(n^3)
        # O(n) space complexity because we are creating a substring variable that is the length of the string s which is O(n)
        # and we are creating a longest_palindrome variable that is the length of the string s which is O(n)  


        longest_palindrome = ""              # empty string
        for i in range(len(s)):                        # range of the length of the string s    
            for j in range(i, len(s)):                # i is the starting index and j is the ending index
                substring = s[i:j+1]                   #  +1 because we want to include the last character in the substring ":j+1" 
                if substring == substring[::-1]:            # if the substring is a palindrome. [::-1] reverses the string
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring
        return longest_palindrome
    
       

        # 1. find all substrings
        # 2. check if each substring is a palindrome
        # 3. if it is, check if it's longer than the current longest palindrome substring
        # 4. if it is, replace the current longest palindrome substring with the current substring
# test program
s = "tracecars"
print(str(solution().longestPalindrome(s)))
# racecar


# what is wrong with this code?

