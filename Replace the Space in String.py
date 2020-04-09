# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

# 示例 1：

# 输入：s = "We are happy."
# 输出："We%20are%20happy."

# Answer:

class Solution:
    def replaceSpace(self, s: str) -> str:
        ss = ''
        for i in range(len(s)):
            if s[i] == ' ':
                ss = ss + "%20"
            else:
                ss = ss + s[i]
        return ss

