class Solution:
    def search(self, nums, target):

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[lo] <= nums[mid]:

                # Target lies inside left half
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Right half is sorted
            else:

                # Target lies inside right half
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1