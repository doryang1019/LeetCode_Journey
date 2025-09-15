// Runtime 3ms
// Beats 91.23%

// Memory 44.96MB
// Beats 17.06%

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        char[] sArray = s.toCharArray();
        Arrays.sort(sArray);

        char[] tArray = t.toCharArray();
        Arrays.sort(tArray);

        return (new String(sArray)).equals(new String(tArray));
    }
}