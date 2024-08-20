'''
provides the heap data structure that is mainly used to represent a priority queue.
The proprty of this data structure is that it always give the smallest element whenever the element is popped.

'''
import heapq

li = [5, 7, 9, 1, 3]
heapq.heapify(li)

print("The created heap is : ", end="")
print(list(li))

heapq.heappush(li, 4)

print("The modified heap after push is : ", end="")
print(list(li))

print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
