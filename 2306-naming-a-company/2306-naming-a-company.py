class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        A = [set() for _ in range(26)]
        count = 0
        
        for idea in ideas:
            A[ord(idea[0]) - ord('a')].add(idea[1:])
        
        for i in range(25):
            for j in range(i+1, 26):
                k = len(A[i] & A[j])
                count += 2 * (len(A[i])-k) * (len(A[j])-k)        
        return count
                
            