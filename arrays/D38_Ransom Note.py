class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for ch in ransomNote:

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True
    