"""
Bubble Sort:

A naive sorting that compares and swaps adjacent elements

Time Complexity: O(n**2)
Space Complexity: O(1)

"""

def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order and this sorted list is then returned.

    :param seq: A list of integers
    :return: A list of sorted integers

    """

    l = len(seq)

    for i in range(l):
        for n in range(1, l-1):
            if seq[n] < seq[n-1]:
                seq[n-1], seq[n] = seq[n], seq[n-1]
        print(seq)

    return seq

print("final seq:", sort([349, 85, 785, 56, 94, 83]))

