class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n=max(nums)
        m=min(nums)
        res=0
        for i in range (1,m+1):
            if n%i==0:
                if m%i==0:
                    res=max(res,i)
        return res
