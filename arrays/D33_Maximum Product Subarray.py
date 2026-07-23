class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            # If current number is negative, swap max and min
            if nums[i] < 0:
                currentMax, currentMin = currentMin, currentMax

             # Update current maximum product
            currentMax = max(nums[i], currentMax * nums[i])

             # Update current minimum product
            currentMin = min(nums[i], currentMin * nums[i])

             # Update overall answer
            answer = max(answer, currentMax)
