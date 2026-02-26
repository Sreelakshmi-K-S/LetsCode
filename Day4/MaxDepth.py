class Solution(object):
    def maxDepth(self, s):
        sum=0
        max=0
        for i in range (len(s)):
            if s[i]=="(":
                sum+=1
                if max<sum:
                 max= sum
            elif s[i]==")":
                sum-=1
        return max
