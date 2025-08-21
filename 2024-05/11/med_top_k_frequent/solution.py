import heapq

k = 2
nums = [1,2,2,3,3,3]

freq = {}
for num in nums:
    if num in freq: freq[num] += 1
    else: freq[num] = 1

heap = []
for num in freq.keys():
    heapq.heappush(heap, (freq[num], num)) # push with count first -> count-based minheap
    if len(heap) > k:
        heapq.heappop(heap) 

res = []
print(len(heap))
for i in range(len(heap)):
    res.append(list(heapq.heappop(heap)[1]))

print(res)



