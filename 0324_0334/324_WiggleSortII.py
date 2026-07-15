import heapq
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hqs = []
        hql = []
        for n in nums:
            heapq.heappush(hqs, -n)
            heapq.heappush(hql, -heapq.heappop(hqs))
            if len(hql) > len(hqs):
                heapq.heappush(hqs, -heapq.heappop(hql))
        print(hqs)
        print(hql)
        s = []
        while hqs:
            s.append(-heapq.heappop(hqs))
        l = []
        while hql:
            l.append(heapq.heappop(hql))
        s.reverse()
        print(s)
        print(l)

        i = 0
        while i < len(nums) // 2:
            nums[i * 2] = s.pop()
            nums[i * 2 + 1] = l.pop()
            i += 1
        if s:
            nums[-1] = s.pop()
        return nums

s = Solution()
print(s.wiggleSort([1, 5, 1, 1, 6, 4]))
print(s.wiggleSort([1,4,3,4,1,2,1,3,1,3,2,3,3]))
