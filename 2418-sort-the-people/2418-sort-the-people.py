class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for _ in range(n):
            l = [(j,i) for i, j in zip(names,heights)]
        l.sort(reverse=True)
        return [x[1] for x in l]
        