# Write a function that, given a sentence like the one above, along with the position of the opening paranthesis, finds the corresponding closing paranthesis

# Example: If the example string above is input with number10(position of the firs paranthesis) the output should be 79(position of the last paranthesis)

# We can do this in O(n) time
# O(1) addiotional space


def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0

    for position in range(opening_paren_index + 1, len(sentence)):
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

    raise Exception('No closing parenthesis :(')


# Complexity
# O(n) time and O(1) space

# the trick to many 'parsing' question like this is using a stack to track which
# brackets/phrases/etc are 'open' as you go

# so next time you get a parsing a question, one of your thoughts should be "use a stack!"

# Tests


