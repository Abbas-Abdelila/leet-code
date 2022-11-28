class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Matches -> [[1,3], [2,4],[3,1],[5,6]]
        winners = ([x[0] for x in matches])
        lossers = ([x[1] for x in matches])
        
        invincibles = list(set(winners)-set(lossers))
        opps = []
        loss_dict = collections.Counter(lossers)
        for player in loss_dict:
            if loss_dict[player] == 1:
                opps.append(player)
        
        return [sorted(invincibles), sorted(opps)]
