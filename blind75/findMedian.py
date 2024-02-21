# find the median of a data stream 

import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.small , self.large = [] , []
        #these heaps are max and min heaps
    
    def add_num(self, num) -> None:
        heapq.heappush(self.small,-1*num)

        if (self.small and self.large and (-1*self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if(len(self.small) > len(self.large)+1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if(len(self.small)+1  < len(self.large)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
    
    def findMedian(self) -> float:
        if(len(self.small) > len(self.large)):
            return -1* self.small[0]
        if(len(self.small) < len(self.large)):
            return self.large[0]
        return ((-1* self.small[0] + self.large[0]) /2) 