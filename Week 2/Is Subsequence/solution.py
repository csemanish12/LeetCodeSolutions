class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = 0
        index = 0
        if not s:
            return True
        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1
                counter += 1
            if index+1 > len(s):
                break
        return counter == len(s)



s = "axc"
t = "ahbgxdc"
obj = Solution()
print(obj.isSubsequence(s, t))