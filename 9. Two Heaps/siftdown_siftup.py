def f(heap, a, b):
    # tl;dr: swap the new item with its parent while it is appropriate
    # (new item is smaller than its parent)
    # `swim method`, shift the item up until it is in the right place
    # sift down: the bubbles move down (even though the elem swims up)
    e = heap[b]
    while b > a:
        c = (b - 1) >> 1
        d = heap[c]
        if e < d:
            heap[b] = d
            b = c
            continue
        break
    heap[b] = e


def g(heap, a):
    # put elem all the way down by swapping with its child, then `swim` it up
    # sift up: the bubbles move up (even though the elem sinks)
    b = len(heap)
    c = a
    d = heap[a]
    e = 2 * a + 1
    while e < b:
        # if the 2 kids are equal, you want to swap with the right one (bigger one)?
        h = e + 1
        if h < b and not heap[e] < heap[h]:
            e = h
        heap[a] = heap[e]
        a = e
        e = 2 * a + 1
    heap[a] = d
    f(heap, c, a)
