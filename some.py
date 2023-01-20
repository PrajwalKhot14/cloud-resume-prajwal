from collections import deque

def func(l):
    minl = [-1] * len(l)
    minr = [len(l)] * len(l)

    stack = deque()
    stack.append((-1, -1))
    for idx, val in enumerate(l):
        while stack[-1][1] > val:
            stack.pop()
        minl[idx] = stack[-1][0]
        stack.append((idx, val))

    stack = deque()
    stack.append((len(l), -1))
    for idx in range(len(l) - 1, -1, -1):
        while stack[-1][1] > val:
            stack.pop()
        minr[idx] = stack[-1][0]
        stack.append((idx, val))


    endswith = [0] * len(l)
    endswith[0] = l[0]
    for i in range(1, len(l)):
        endswith[i] = (
            l[i]
            +
            i * l[i]
            +
            l[i-1]
        )

    for i in range(1, len(l)):
        endswith[i] = endswith[i] + endswith[i-1]

    startswith = [0] * len(l)
    startswith[-1] = l[-1]
    for i in range(len(l) -2 , -1, -1):
        startswith[i] = (
            l[i]
            +
            (len(l) - i - 1) * l[i]
            +
            l[i+1]
        )

    for i in range(len(l) - 2, -1, -1):
        startswith[i] = startswith[i] + startswith[i+1]

    for idx in range(len(l)):

