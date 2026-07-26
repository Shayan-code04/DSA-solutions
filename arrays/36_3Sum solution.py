'''Given an integer array nums, return
all the triplets [nums[i], nums[j], 
nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.'''



'''sliding Window'''


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        ''' Fix one number at a time'''
        for i in range(len(nums) - 2):

            #Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers
                    left += 1
                    right -= 1

                elif total < 0:
                    # Need a larger sum
                    left += 1

                else:
                    # Need a smaller sum
                    right -= 1

        return result