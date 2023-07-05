# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

# Here's some examples and some starter code.

def reverse_integer(num):
    # Fill this in.
    if num < 0:
        return -1 * reverse_integer(-num)
    result = 0
    while num:
        result = (result * 10) + (num % 10)
        num //= 10
    return result

print(reverse_integer(135)) 
# 531

print(reverse_integer(-321))
# -123