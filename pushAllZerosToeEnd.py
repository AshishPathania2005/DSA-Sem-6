def push_zeros_to_end(arr):
    n = len(arr)
    count = 0  # Count of non-zero elements

    # Traverse the array. If the element is non-zero, then
    # replace the element at index 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to the front
    # and 'count' is set as the index of the first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

    return arr

     