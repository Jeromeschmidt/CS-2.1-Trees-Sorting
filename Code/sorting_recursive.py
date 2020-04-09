#!python
from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    if len(items1) == 0:
        return items2
    if len(items2) == 0:
        return items1
    i = 0
    j = 0
    result = list()

    while ((i < len(items1)) and (j < len(items2))):
        if items1[i] < items2[j]:
            result.append(items1[i])
            i += 1
        elif items1[i] > items2[j]:
            result.append(items2[j])
            j += 1
        else:
            result.append(items1[i])
            result.append(items2[j])
            i += 1
            j += 1

    if i < len(items1):
        for i in range(i, len(items1)):
            result.append(items1[i])
    if j < len(items2):
        for j in range(j, len(items2)):
            result.append(items2[j])

    return result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 4:
        return insertion_sort(items)
    else:
        return merge(split_sort_merge(items[:int(len(items)/2)]), split_sort_merge(items[int(len(items)/2):]))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) == 1 or len(items) == 0:
        return items
    # TODO: Split items list into approximately equal halves
    # print(items)
    return merge(merge_sort(items[:int(len(items)/2)]), merge_sort(items[int(len(items)/2):]))
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (Choosing element in the middle) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_index = low
    for i in range(low, high+1):
        if items[i] <= items[pivot_index]:
            items[low], items[i] = items[i], items[low]
            i += 1
    return pivot_index



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if high is None:
        high = len(items)-1
    if low is None:
        low = 0

    if low < high:

        pt = partition(items, low, high)

        quick_sort(items, low, pt-1)
        quick_sort(items, pt+1, high)
    return items

# merge_sort([1,3,5,2,4,6,3])
# print(merge_sort([1,3,5,2,4,6,3]))
print(quick_sort([1,3,5,2,4,6,3]))
# print(quick_sort([5,7,1,3,4,6,3]))
