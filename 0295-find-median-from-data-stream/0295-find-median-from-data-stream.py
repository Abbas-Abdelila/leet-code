from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.arr = SortedList()
        self.n = 0

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.arr[self.n//2 - 1] + self.arr[self.n//2])/2
        else:
            return self.arr[self.n//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()