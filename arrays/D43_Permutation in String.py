class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
              # Step 1: If s1 is longer than s2, it's impossible
        if len(s1) > len(s2):
            return False

        # Step 2: Count the frequency of characters in s1
        s1_count = Counter(s1)

        # Step 3: Count the frequency of the first window in s2
        window = Counter(s2[:len(s1)])

        # Step 4: Check if the first window is already a permutation
        if window == s1_count:
            return True

        # Step 5: Left pointer of the sliding window
        left = 0
         # Step 6: Slide the window through s2
        for right in range(len(s1), len(s2)):

            # Add the new character entering the window
            window[s2[right]] += 1

            # Remove the old character leaving the window
            window[s2[left]] -= 1

            # Remove the key if its count becomes 0
            if window[s2[left]] == 0:
                del window[s2[left]]

            # Move the left pointer
            left += 1

            # Compare the frequency maps
            if window == s1_count:
                return True

        return False    