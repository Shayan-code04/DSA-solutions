class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        def backtracking(start,remaining):
            if remaining ==0:
                result.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(start,len(candidates)) :
                path.append(candidates[i])
                backtracking(i,remaining-candidates[i])
                path.pop()
        backtracking(0,target)



        return result

