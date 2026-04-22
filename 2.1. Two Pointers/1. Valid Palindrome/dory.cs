// Runtime 35ms
// Beats 23.99%

// Memory 46.18MB
// Beats 34.84%

public class Solution {
    public bool IsPalindrome(string s) {
        string result = new string(s.Where(c => char.IsLetter(c)).ToArray()).ToLower();

        // If considering number 
        // string result = new string(s.Where(c => char.IsLetterOrDigit(c)).ToArray()).ToLowerInvariant();

        if(result.Length <= 1) {
            return true;
        }
        int start = 0;
        int end = result.Length - 1;
        while(start < end) {
            if(result[start] == result[end]) {
                start++;
                end--;
            } else {
                return false;
            }
        }
        return true;
    }
}