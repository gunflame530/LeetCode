# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Answer：

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen = 1
        head = 0                                # Sliding window
        tail = head + 1
        while tail < len(s):
            repeat = False                      # Flag
            for i in range(tail - head):        
                if s[head + i] == s[tail]:
                    repeat = True               # if the last character of the sliding window has already existed in the window, repeat is True
            if not repeat:                      # if it is a substring without repeating chars
                if maxlen < tail - head + 1:    # update the maximum of the length
                    maxlen = tail - head + 1
                tail = tail + 1                 # tail move forward
            else:
                head = head + 1                 # if repeated, head move forward
                if head == tail:                # the width of the window must be larger than 1
                    tail = tail + 1
        return maxlen
