class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo={}

        return self.solve(nums, 0)

    def solve(self,nums,i):
        if i>= len(nums):
            return 0
        if i in self.memo:
            return self.memo[i]
        rob = nums[i] + self.solve(nums, i + 2)

        skip = self.solve(nums, i + 1)

        self.memo[i] = max(rob, skip)

        return self.memo[i]                      