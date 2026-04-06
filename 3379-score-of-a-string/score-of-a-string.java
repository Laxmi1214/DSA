class Solution {
    public int scoreOfString(String s) {
        int[] arr = new int[s.length() - 1];
        int p = 0;
        int q = 1;

        for(int i=0; i<s.length() - 1; i++){
            int diff = Math.abs(s.charAt(q) - s.charAt(p));
            
            arr[i] = diff;
            p++;
            q++;
        }
        int sum = 0;
        for(int x : arr){
            sum += x;
        }

        return sum;
        
    }
}