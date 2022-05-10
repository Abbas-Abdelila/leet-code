class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        def dfs(digit, start_num, cur, cur_sum):
            
            if n==cur_sum and digit == k:
                ans.append(cur[:])
            
            elif digit >= k or cur_sum > n:
                return
            
            else:
                for i in range(start_num+1, 10):
                    cur.append(i)
                    dfs(digit+1, i, cur, cur_sum+i)
                    cur.pop()
        
        ans = []
        dfs(0,0,[],0)
        
        return ans

            