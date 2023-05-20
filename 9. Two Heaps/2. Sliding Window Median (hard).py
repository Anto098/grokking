from heapq import *
import heapq

class SlidingWindowMedian:
    max_heap = []
    min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []
        if len(nums) < k:
            return result
        p1 = 0
        for i in range(p1, p1 + k):
            self.insert_num(nums[i])
        while True:
            # how to do a `do while` in python:
            # do a `while true`, put your condition later in the while loop
            result.append(self.find_median())
            if nums[p1] > -self.max_heap[0]:
                self.remove_num(self.min_heap, nums[p1])
            else:
                self.remove_num(self.max_heap, -nums[p1])
            if p1 + k >= len(nums):
                break
            self.insert_num(nums[p1 + k])
            p1 += 1
        return result

    def remove_num(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[0]
        heap.pop(0)

        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

        self.balance_heaps()


    def insert_num(self, num):
        # we need to insert negative numbers into the max_heap because `heapq`
        # is a min heap data structure by definition
        if not self.max_heap or -num >= self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        self.balance_heaps()

    def balance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


if __name__ == "__main__":
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print(f"Sliding window medians are: {result}")

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print(f"Sliding window medians are: {result}")
