from collections import deque
import sys

def push(x) :
    queue.append(x)

def pop() :
    if len(queue) > 0 :
        print(queue[0])
        queue.popleft()
    else:
        print(-1)

def size() :
    print(len(queue))

def empty() :
    if len(queue) > 0 :
        print(0)
    else :
        print(1)

def front() :
    if len(queue) > 0:
        print(queue[0])
    else :
        print(-1)

def back() :
    if len(queue) > 0:
        print(queue[-1])
    else :
        print(-1)

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n) :
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        size()
    elif order[0] == 'empty':
        empty()
    elif order[0] == 'front':
        front()
    elif order[0] == 'back':
        back()