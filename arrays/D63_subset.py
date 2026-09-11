class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(start):
            # Every path is a valid subset
            result.append(path.copy())

            for i in range(start, len(nums)):
                # Make the choice
                path.append(nums[i])

                # Explore
                backtracking(i + 1)

                # Undo the choice
                path.pop()

        backtracking(0)

        return result

    