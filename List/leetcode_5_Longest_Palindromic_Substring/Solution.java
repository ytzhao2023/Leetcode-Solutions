package List.leetcode_5_Longest_Palindromic_Substring;

class Solution {
    private int start, end;

    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {
            return " ";
        }

        for (int i = 0; i < s.length(); i++) {
            expandAroundCenter(s, i, i);
            expandAroundCenter(s, i, i+1);
        }

        return s.substring(start, end + 1);    
    }

    private void expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        if (right - left - 2 > end - start){
            start = left + 1;
            end = right - 1; 
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.longestPalindrome("vabavb");
        System.out.println(result);
    }
}