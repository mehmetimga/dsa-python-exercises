from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_chat = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index: int, path: str):
            if index == len(digits):
                combinations.append(path)
                return
            possible_chars = digit_to_chat[digits[index]]
            for char in possible_chars:
                backtrack(index + 1, path + char)       
                
        combinations = []
        backtrack(0, "")
        return combinations
# Example usage:
solution = Solution()

print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))  # Output: []
print(solution.letterCombinations("2"))  # Output: ["a","b","c"]        