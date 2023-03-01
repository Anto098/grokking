def merge(a, b):
    merged = []
    p1, p2 = 0, 0
    while p1 < len(a) and p2 < len(b):
        ca, cb = a[p1], b[p2]
        if ca[1] < cb[0]:
            p1 += 1
        elif ca[0] > cb[1]:
            p2 += 1
        else:
            s = max(ca[0], cb[0])
            e = min(ca[1], cb[1])
            merged.append([s, e])
            if ca[1] <= cb[1]:
                p1 += 1
            if ca[1] >= cb[1]:
                p2 += 1

    return merged


if __name__ == "__main__":
    print(f"Intervals Intersection: {merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])}")
    print(f"Intervals Intersection: {merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])}")
