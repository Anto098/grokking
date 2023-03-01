class MedianOfAStream:
    def insert_num(self, num):
        return -1

    def find_median(self):
        return 0.0


if __name__ == "__main__":
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print(f"The median is {medianOfAStream.find_median()}")
    medianOfAStream.insert_num(5)
    print(f"The median is {medianOfAStream.find_median()}")
    medianOfAStream.insert_num(4)
    print(f"The median is {medianOfAStream.find_median()}")