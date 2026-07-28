class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert the list into a set for O(1) lookups
        numSet = set(nums)

        # Stores the longest sequence found
        longest = 0

        # Check every unique number
        for num in numSet:

            # Start only if this is the beginning of a sequence
            if num - 1 not in numSet:

                current = num
                length = 1

                # Keep extending the sequence
                while current + 1 in numSet:
                    current += 1
                    length += 1

                # Update the longest sequence
                longest = max(longest, length)

        # Return the answer
        return longest