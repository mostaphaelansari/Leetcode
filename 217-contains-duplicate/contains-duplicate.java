class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniqueNumbers = new HashSet<>();
        for (int num : nums) {
            if (!uniqueNumbers.add(num)) { // If add() returns false, a duplicate exists
                return true;
            }
        }
        return false;
    }
}