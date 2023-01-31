class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i],ages[i]] for i in range(len(scores))]
        pairs.sort() #sorts according to scores

        #Intuition - what would be the maximum score at i'th place by selecting i'th player

        dp = [pairs[i][0] for i in range(len(scores))]

        for i in range(1,len(scores)):
            for j in range(i-1,-1,-1):
                if pairs[j][1]<=pairs[i][1]:
                    dp[i] = max(dp[i],pairs[i][0]+dp[j])

        return max(dp)