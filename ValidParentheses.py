class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        """
        # have a stack and keep track of all the opening charcters that will be added to it
        stack = []
        check = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for c in s:
            # if the character is in a closing one
            if c in check:
                # check if there is still something in the stack and the last character in the stack is equal to the corresponding character in the hashtable and if it all checks out remove it from the stack
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    # if there is something wrong like the stack is empty or the charcters dont match up return False
                    return False
            else:
                # if its an opening character add it to the stack
                stack.append(c)
        # finally once you get through the loop if there isnt a stack return True because everything had a matching pair otherwise return False
        return True if not stack else False
