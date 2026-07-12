

def contains_duplicate(nums):
    # Brute force: O(n^2) time, O(1) space — nested loop compares every pair
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def contains_duplicate_optimized(nums):
    # Optimized: O(n) time, O(n) space — trade space for time using a set
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def main():
    print("Brute Force:")
    print(contains_duplicate([1, 2, 3, 1]))  # True
    print(contains_duplicate([1, 2, 3, 4]))  # False
    print(contains_duplicate([1, 1, 1]))     # True
    print(contains_duplicate([]))            # False
    print(contains_duplicate([5]))           # False

    print("Optimized:")
    print(contains_duplicate_optimized([1, 2, 3, 1]))  # True
    print(contains_duplicate_optimized([1, 2, 3, 4]))  # False
    print(contains_duplicate_optimized([1, 1, 1]))     # True
    print(contains_duplicate_optimized([]))            # False
    print(contains_duplicate_optimized([5]))           # False
if __name__ == "__main__":
    main()