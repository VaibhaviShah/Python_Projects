"""
Merge Sort:

Uses divide and Conquer to recursively divide and sort the list
Time Complexity: O(n log n)

"""

def merge(left, right):
    """
    Takes two sorted sub lists and merges them in to a single sorted sub list and returns it.

    :param left: A list of sorted integers
    :param right: A list of Sorted integers
    :return: A list of sorted integers
    """

    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result

def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted list is then returned.
    :param seq: A list of integers
    :return: A list of sorted integers
    """

    if len(seq) <= 1:
        return seq

    middle = int(len(seq)/ 2)
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)

print(sort([23, 45, 22, 44, 996, 345, 95, 1]))