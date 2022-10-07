class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int start = 0, end = letters.length;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (letters[mid] <= target) start = mid + 1;
            else end = mid;
        }
        return letters[start % letters.length]; // modulo because the target may be bigger than every char in the array(and it will print the first index)
    }
}