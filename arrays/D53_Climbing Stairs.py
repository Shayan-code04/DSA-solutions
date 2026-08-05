class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a memo array of size n + 1
        self.memo = [0] * (n + 1)

        return self.solve(n)

    def solve(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1

        if n == 2:
            return 2

        # If already computed, return stored answer
        if self.memo[n] != 0:
            return self.memo[n]

        # Compute, store, and return
        self.memo[n] = self.solve(n - 1) + self.solve(n - 2)

        return self.memo[n]
    