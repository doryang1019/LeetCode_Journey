// Runtime 31ms
// Beats 24.36%

// Memory 44.72MB
// Beats 12.57%

public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) {
            return false;
        }
        char[] s_char = s.ToCharArray();
        char[] t_char = t.ToCharArray();
        Array.Sort(s_char);
        Array.Sort(t_char);
        return new string(s_char) == new string(t_char);
    }
}