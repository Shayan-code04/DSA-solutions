def two_sum_bruteforce(nums, target):
    """
    Brute Force Approach

    Compare every possible pair of numbers in the array.
    If the sum of two numbers equals the target,
    return their indices.

    Time Complexity:
    O(n²)
    Because for every element, we compare it with all the remaining elements.

    Space Complexity:
    O(1)
    No extra data structure is used.
    """

    # Traverse through each element
    for i in range(len(nums)):

        # Compare it with every element after it
        for j in range(i + 1, len(nums)):

            # Check if the pair adds up to the target
            if nums[i] + nums[j] == target:

                # Return the indices of the two numbers
                return [i, j]

def two_sum_optimized(nums, target):
    """
    Optimized Approach (Hash Map)

    Single pass through the array. For each number, check if its
    complement (target - number) already exists in the hash map.
    If it does, return the current index and the complement's index.
    Otherwise, store the number and its index in the map.

    Time Complexity:
    O(n)
    Single pass through the array; hash map lookups are O(1).

    Space Complexity:
    O(n)
    Hash map can store up to n elements.
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
# -------------------------
# Test Cases
# -------------------------
def main():
    nums1 = [2, 7, 11, 15]
    target1 = 9

    nums2 = [3, 2, 4]
    target2 = 6

    nums3 = [3, 2, 4, 3]
    target3 = 7 

    num4 = [0]
    target4 = 0

    num5 = []
    target5 = 0

    print(two_sum_bruteforce(nums1, target1))   # [0, 1]
    print(two_sum_bruteforce(nums2, target2))   # [1, 2]
    print(two_sum_bruteforce(nums3, target3))   # [0, 2]
    print(two_sum_bruteforce(num4, target4))    # None (no pair possible)
    print(two_sum_bruteforce(num5, target5))    # None (empty array)
    print(two_sum_optimized(nums1, target1))     # [0, 1]
    print(two_sum_optimized(nums2, target2))   # [1, 2]
    print(two_sum_optimized(nums3, target3))   # [0, 2]
    print(two_sum_optimized(num4, target4))    # [] (no pair possible)
    print(two_sum_optimized(num5, target5))    # [] (empty array)

if __name__ == "__main__":
    main()