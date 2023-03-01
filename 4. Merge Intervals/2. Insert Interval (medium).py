def insert(intervals, new_interval):
    i = 0
    while intervals[i][0] < new_interval[0]:
        i += 1
    else:
        intervals.insert(i, new_interval)

    return merge(intervals)


def merge(intervals):
    i = 0

    while i < len(intervals) - 1 and len(intervals) > 1:
        if intervals[i + 1][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.pop(i + 1)
        else:
            i += 1

    return intervals


if __name__ == "__main__":
    print(f"Intervals after inserting the new interval: {insert([[1, 3], [5, 7], [8, 12]], [4, 6])}")
    print(f"Intervals after inserting the new interval: {insert([[1, 3], [5, 7], [8, 12]], [4, 10])}")
    print(f"Intervals after inserting the new interval: {insert([[5, 7]], [1, 4])}")
