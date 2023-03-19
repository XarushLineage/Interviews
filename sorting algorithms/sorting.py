def bubble_sort(arr):
    """
    Implementation of bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    """
    Implementation of quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

def balloon_sort(arr):
    """
    Implementation of balloon sort algorithm.
    """
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def radix_sort(arr):
    """
    Implementation of radix sort algorithm.
    """
    max_val = max(arr)
    exp = 1
    while max_val / exp > 0:
        count = [0] * 10
        for i in arr:
            count[int(i / exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        output = [0] * len(arr)
        for i in reversed(arr):
            output[count[int(i / exp) % 10] - 1] = i
            count[int(i / exp) % 10] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
        exp *= 10

# Prompt the user to enter a list of integers
arr = input("Enter a list of integers, separated by spaces: ")
arr = [int(x) for x in arr.split()]

# Sort the list using bubble sort
bubble_sort_arr = arr.copy()
bubble_sort(bubble_sort_arr)
print("Bubble sort:", bubble_sort_arr)

# Sort the list using quick sort
quick_sort_arr = arr.copy()
quick_sort_arr = quick_sort(quick_sort_arr)
print("Quick sort:", quick_sort_arr)

# Sort the list using balloon sort
balloon_sort_arr = arr.copy()
balloon_sort_arr = balloon_sort(balloon_sort_arr)
print("Balloon sort:", balloon_sort_arr)

# Sort the list using radix sort
radix_sort_arr = arr.copy()
radix_sort(radix_sort_arr)
print("Radix sort:", radix_sort_arr)
