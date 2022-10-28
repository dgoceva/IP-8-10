import collections


from collections import deque

fifo = deque(map(int, input('input queue: ').split()))
print(fifo)
fifo.append(11)
fifo.append(22)
print(fifo)

print(fifo.popleft())
print(fifo.popleft())
print(fifo)

fifo = deque("abcdef")
print(fifo)
