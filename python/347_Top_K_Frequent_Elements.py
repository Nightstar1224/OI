# avs
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        minHeap = []
        for n, count in counter.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, n))
            elif count > minHeap[0][0]:
                heapq.heappushpop(minHeap, (count, n))
        topK = [n for count, n in minHeap]
        return topK