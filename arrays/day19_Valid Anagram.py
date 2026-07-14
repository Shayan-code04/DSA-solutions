class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Different lengths -> cannot be anagrams
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in first string
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Remove counts using second string
        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
    

def main():
     solution=Solution()


     
     print(solution.isAnagram(s="anagram",t="nagaram")) # True
     print(solution.isAnagram(s="anagra", t="nagara"))
     print(solution.isAnagram(s="anagram", t="nagarui"))
     print(solution.isAnagram(s="ammgram",t="mmmgraa"))           


if __name__ == "__main__":
    main()

""" Time Complexity: O(n)

Space Complexity: O(k)"""