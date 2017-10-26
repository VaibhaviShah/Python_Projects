"""
Quick Sort:

Uses partitioning to recursively divide and sort a list
Time Complexity: O(n**2) worst case
Space Complexity: O(n**2)

"""

def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. this sorted list is then returned.
    :param seq: A list of integers
    :return: A list of sorted integers
    """
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [],[]
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)


print(sort([85, 349, 56, 94, 785, 83]))
