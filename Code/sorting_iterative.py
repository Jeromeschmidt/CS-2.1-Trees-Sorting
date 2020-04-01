#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) Why and under what conditions? Worst case, visits each element n times for each element
    TODO: Memory usage: O(n) Why and under what conditions? No new memory created, elements are swapped"""
    # TODO: Repeat until all items are in sorted order
    swapped = True
    last_unsorted = len(items)-1

    while swapped == True:
        swapped = False
        for i in range(last_unsorted):
            # TODO: Swap adjacent items that are out of order
            if (items[i] > items[i+1]):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        last_unsorted -= 1
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    for i in range(len(items)):
        minimum_index = i
        # TODO: Find minimum item in unsorted items
        for j in range(i+1, len(items), 1):
            if items[j] < items[minimum_index]:
                minimum_index = j
    # TODO: Swap it with first unsorted item
        items[i], items[minimum_index] = items[minimum_index], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(1, len(items)):
        j = i-1
        temp = items[i]
        while ((j >= 0) and (items[j] > temp)):
            items[j+1] = items[j]
            j -= 1
        items[j+1] = temp
    return items
