"""
Selection Sort:

A sorting that uses in-place comparision

Time Complexity: O(n**2)
Space Complexity: O(1)
"""

def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted list is then returned.

    :param seq: A list of Integers
    :return: A list of Sorted Integers
    """

    for i in range(0, len(seq)):
        iMin = i
        for j in range(i+1, len(seq)):
            if seq[iMin] > seq[j]:
                iMin = j
        if i != iMin:
            seq[i], seq[iMin] = seq[iMin], seq[i]
    return seq

print(sort([85, 349, 56, 94, 785, 83]))
