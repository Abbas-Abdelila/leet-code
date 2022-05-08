# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def iterator(nestedList):
            for item in nestedList:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    for sub_item in iterator(item.getList()):
                        yield sub_item
                        
        self.value = None
        self.list = iterator(nestedList)
    
    def next(self) -> int:
        return self.value
    
    def hasNext(self) -> bool:
        self.value = next(self.list, None)
        if self.value is not None:
            return True
        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())