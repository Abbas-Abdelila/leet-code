class UndergroundSystem:

    def __init__(self):
        self.users = defaultdict()
        self.stats = defaultdict(lambda:[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = (stationName, t)    

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn, time = self.users[id]
        self.stats[(checkIn, stationName)][0] += t-time
        self.stats[(checkIn, stationName)][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stats[(startStation, endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)