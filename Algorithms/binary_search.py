"""
Binary Search:

Recursively partitions the list until the 'key' is found
Time Complexity: O(log n)

"""

def search(seq, key):
    """
    Takes a list of integers and searches if the 'key' is contained within the list
    :param seq: A list of Integers
    :param key: The integer to be searched for
    :return: The index of where the 'key' is located in the list
            If 'key' is not found then False is returned.
    """

    low = 0
    high = len(seq) - 1
    print("High: ", high)

    while high >= low:
        mid = low + (high - low) // 2
        print("Mid", mid)
        if seq[mid] < key:
            low = mid + 1
        elif seq[mid] > key:
            high = mid - 1
        else:
            return mid
    return False

print(search([1,2,6,4,8,6,9], 6))
print(search([1,2,6,4,8,6,9], 9))
