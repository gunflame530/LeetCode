# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

# Answer:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        if s == "":
            return 0
        isWord = 0           # if the end of the string is space characters
        for i in range(len(s)):
            if s[len(s) - i - 1] == ' ':
                if isWord == 0:
                    continue
                else:
                    return length
            isWord = 1
            length = length + 1

        return length
