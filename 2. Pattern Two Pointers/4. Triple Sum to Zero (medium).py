"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(l):
    l.sort()
    triplets = []

    for i in range(len(l)):
        if l > 0 and l[i] == l[i - 1]:
            continue

        start = i + 1
        target = -l[i]
        end = len(l) - 1
        while start < end:
            if l[start] + l[end] == target:
                triplets.append([l[i], l[start], l[end]])
                start += 1
                end -= 1

                while start > 0 and l[start] == l[start - 1]:
                    start += 1
                while end < len(l) - 1 and l[end] == l[end + 1]:
                    end -= 1

            elif l[start] + l[end] > target:
                end -= 1
            else:
                start += 1

    return triplets


if __name__ == "__main__":
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
