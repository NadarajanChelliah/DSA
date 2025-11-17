class Solution(object):
    #sample inputs :
    #"101"
    #"111111"
    def numSub(self, s):
        MOD = 10**9 + 7
        res = 0
        cons = 0
        for i in s:
            if i == "1":
                cons += 1
                res =(res + cons) % MOD 
            else:
                cons = 0

        return res
    

sol = Solution()
print(sol.numSub("0110111"))    
        