class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // If concatenating str1 and str2 in different orders gives different results, return ""
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        
        // Find the greatest common divisor of the lengths of str1 and str2
        int gcdLength = gcd(str1.length(), str2.length());
        
        // The result is the prefix of str1 with length equal to the GCD of the lengths
        return str1.substring(0, gcdLength);
    }
    
    // Helper method to calculate the GCD of two numbers
    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}
