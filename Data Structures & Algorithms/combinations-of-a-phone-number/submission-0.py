class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if not digits:
            return res

        def dfs(i, cur):
            if i == len(digits):
                res.append(cur[:])
                return
            
            for c in digit_to_letter[digits[i]]:
                dfs(i + 1, cur + c)
        
        dfs(0, "")

        return res