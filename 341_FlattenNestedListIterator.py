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
    def __init__(self, nestedList):
        # 逆順で積む
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext() により、先頭は必ず整数
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            x = self.stack[-1]

            if x.isInteger():
                return True

            # listなら展開する
            self.stack.pop()
            for child in reversed(x.getList()):
                self.stack.append(child)

        return False
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())