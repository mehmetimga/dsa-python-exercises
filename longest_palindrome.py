class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        start, max_length = 0, 1
        
        for i in range(n):
            # Odd length palindromes
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    start = left
                    max_length = current_length
                left -= 1
                right += 1
                
            # Even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > max_length:
                    start = left
                    max_length = current_length
                left -= 1
                right += 1
            
        return s[start:start + max_length]
    
# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"  
