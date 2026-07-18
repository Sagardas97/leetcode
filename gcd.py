l=[2,5,6,9,10]
        
# print(mul(14))
    
class Solution:
    def modulus(self,m,number):
        li=[]
        for i in m:
            li.append(i%number)
        return li
    def mul(self,n):
        r =[]
        for i in range(1,n+1):
            if n%i==0:
                r.append(i)
        return r
    def findGCD(self,nums) -> int:
        mx = min(nums)
        mul = self.mul(mx)
        alls=[]
        for i in mul:
            if set(self.modulus(nums,i))=={0}:
                alls.append(i)
        return max(alls)
    
        
gg = Solution()
print(gg.findGCD(l))
