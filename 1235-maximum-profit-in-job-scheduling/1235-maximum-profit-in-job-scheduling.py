class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start,end,profits = zip(*sorted(zip(startTime,endTime,profit)))
        
        #for each start time, mapp them to next endtime using binseach
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(len(start))}

        #rec(i) = max(profit[i] + rec(i), rec(i+1))
        memo = {}
        
        def rec(i):
            if i == len(start):
                return 0 #we are done, no more profit
            if i in memo:
                return memo[i]
            take = profits[i] + rec(jump[i])
            no_take = rec(i+1)
            res = max(take,no_take)
            memo[i] = res
            return res
        
        return rec(0)

