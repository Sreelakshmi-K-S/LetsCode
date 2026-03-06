class Solution:
    def S(self, n: int) -> int:
        sum=0
        prod=1
        while(n>0):
            dig=n%10
            sum+=dig
            prod*=dig
            n=n//10
        return prod-sum 
