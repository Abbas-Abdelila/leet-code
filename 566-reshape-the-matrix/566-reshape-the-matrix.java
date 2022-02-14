class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int old_c=mat[0].length;
        int old_r=mat.length;
        
        if(old_c*old_r!=r*c)
            return mat;
        
        int ans[][]=new int[r][c];
        
        int c_count=0,r_count=0;
        
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(c_count>=old_c)
                {
                    r_count++;
                    c_count=0;
                }
                ans[i][j]=mat[r_count][c_count++];
            }
        }
        return ans;
    }
}