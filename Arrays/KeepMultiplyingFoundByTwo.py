class Solution(object):
    def findFinalValue(self,nums,original):
        for i in nums:
            if original in nums:
                original *= 2
            else:
                return original

        return original


nums = [5,3,6,1,12]
original = 3

# nums = [2,7,9]
# original = 4
# nums = [2]
# original = 2
sol = Solution()
print(sol.findFinalValue(nums,original))