class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for word in title.split(" "):
            if len(word) > 2:
                ans.append(word.title())
            else:
                ans.append(word.lower())
        
        return " ".join(ans)