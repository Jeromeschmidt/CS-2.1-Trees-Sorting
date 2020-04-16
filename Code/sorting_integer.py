#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n) Why and under what conditions? Every run
    TODO: Memory usage: O(n) Why and under what conditions? Since new memory is created"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if numbers == []:
        return []

    counts = [0] * (max(numbers) + 1)

    for num in numbers:
        counts[num] += 1

    result = list()

    for i in range(len(counts)):
        for j in range(counts[i]):
            result.append((i))

    return result

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if numbers == []:
        return []

    bucket_range = (max(numbers) - min(numbers))/num_buckets
    ranges = list()

    for i in range(num_buckets):
        ranges.append([(min(numbers)+(i*bucket_range)-0.00001),((min(numbers)+(i*bucket_range)-0.00001)+bucket_range)])

    ranges[len(ranges)-1][1] += 1
    buckets = list()

    for i in range(len(ranges)):
        temp = list()
        for j in range(len(numbers)):
            if((numbers[j] >= ranges[i][0]) and (numbers[j] < ranges[i][1])):
                temp.append(numbers[j])
        buckets.append(temp)

    result = list()
    for bucket in buckets:
        result += insertion_sort(bucket)

    return result


print(counting_sort([1,9,3,3,5,3,7,8,9]))
# print(int("5", 36))
# print(counting_sort(["b","a","d","c"]))
# print(ord(chr(int("abc", 36))))
# print(ord(chr(int("a", 36))))
# print(ord(chr(int("b"), 36)))
print(bucket_sort([1,9,3,3,5,3,7,8,9]))
