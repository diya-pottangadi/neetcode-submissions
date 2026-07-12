class Solution {
    public boolean isPalindrome(String s) {
        // 1. strip the white space
        // 2. 2 pointer - one from the left side and one from the right side
        // 3. important! check if the element is alphnumeric, otherwise increment/decrement the counter and check
        // not equal, return false
        // if it makes it through, return true

        String lower = s.replaceAll("\\s+", "");
        String word = lower.toLowerCase();
        if (word.length()<=1){
            return true;
        }
        int left = 0;
        int right = word.length()-1;

        do{
            if(Character.isLetterOrDigit(word.charAt(left)) && Character.isLetterOrDigit(word.charAt(right))){
                if(word.charAt(left) == word.charAt(right)){
                    left++;
                    right--;
                }
                else{
                    return false;
                }
            }
            else if(!Character.isLetterOrDigit(word.charAt(left))){
                left++;
            }
            else{
                right--;
            }
        } while(left<right);
        
        return true;
    }
}
