class Solution {
     public int countOrders(int n) {
        if(n==1) return 1;
        else if(n==2) return 6;
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 6;
        
        long mod = 1000000007;
        for(int i=3;i<=n;i++)
        {
            long k = (long) (i*2 -1);    
            long each = (k*(k+1))/2;     
            long total = each * (long)dp[i-1];    
            dp[i] = (int) (total%mod);
        }
        
        return dp[n];
    }
}