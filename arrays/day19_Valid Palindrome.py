class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare letters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    

def main():
     solution=Solution()

     print(solution.isPalindrome(s="anagram")) 
     print(solution.isPalindrome(s="madam" ))
     print(solution.isPalindrome(s="maam" ))
     print(solution.isPalindrome(s="car"))          


if __name__ == "__main__":
    main()


"""Time Complexity: O(n)

Space Complexity: O(1)"""