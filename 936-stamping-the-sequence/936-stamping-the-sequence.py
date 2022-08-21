class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m = len(stamp)
        n = len(target)
        t = list(target)
        
        indexes = []
        is_done = False
        while not is_done:
            is_done = True
            for i in range(n - m + 1):
                do_stamp = False
                for j in range(m):
                    if t[i + j] == "?":
                        continue
                    if t[i + j] != stamp[j]:
                        do_stamp = False
                        break
                    do_stamp = True
                if do_stamp:
                    for j in range(m):
                        t[i + j] = "?"
                    indexes.append(i)
                    is_done = False
        
        return indexes[::-1] if t == ["?"] * n else []