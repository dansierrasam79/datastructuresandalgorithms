import math

# Define the minimum run size. Lists smaller than this will be sorted entirely by Insertion Sort.
MIN_RUN = 32

def calculate_min_run(n):
    """
    Calculates the minimum run size for Timsort.
    This ensures that N/MIN_RUN is a power of 2, or close to it.
    """
    r = 0       # r will become 1 if the remainder is odd
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    """
    Sorts a small slice of the array using Insertion Sort.
    This is fast for small N or nearly sorted data.
    """
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        # Shift elements greater than temp to the right
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge(arr, l, m, r):
    """
    Merges two sorted runs: arr[l..m] and arr[m+1..r].
    This is the core of the stable sorting mechanism.
    """
    # Lengths of the two runs
    len1, len2 = m - l + 1, r - m
    
    # Create temporary arrays for the runs
    left = arr[l : l + len1]
    right = arr[m + 1 : m + 1 + len2]

    i, j, k = 0, 0, l  # Pointers for left, right, and main array

    # Merge the temp arrays back into arr[l..r]
    while i < len1 and j < len2:
        # Crucial for stability: use <= when elements are equal
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left[] if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining elements of right[] if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

def timsort(arr):
    """
    The main Timsort algorithm. Divides the array into runs and merges them.
    Time Complexity: O(n log n)
    Space Complexity: O(n) (due to temporary arrays in merge)
    """
    n = len(arr)
    if n == 0:
        return

    # 1. Determine the minimum run size
    min_run = calculate_min_run(n)

    # 2. Divide the array into runs and sort them using Insertion Sort
    for i in range(0, n, min_run):
        end = min(i + min_run - 1, n - 1)
        # Apply Insertion Sort to the current run
        insertion_sort(arr, i, end)

    # 3. Start merging runs from size MIN_RUN up to N
    size = min_run
    while size < n:
        # Pick starting point of left run
        for left in range(0, n, 2 * size):
            # Midpoint is the end of the left run
            mid = min(n - 1, left + size - 1)
            # Right is the end of the right run
            right = min((left + 2 * size - 1), (n - 1))

            # Only merge if the runs actually exist
            if mid < right:
                merge(arr, left, mid, right)
        
        # Double the run size for the next pass
        size *= 2

# --- Example Usage ---

if __name__ == "__main__":
    
    # Test case demonstrating stability (tuples)
    # The number is the key, the letter is the tie-breaker
    data = [(3, 'a'), (1, 'c'), (4, 'b'), (1, 'd'), (3, 'e'), (2, 'f')]
    
    print(f"Original Data (Unsorted): {data}")
    
    # Sort the data using Timsort
    timsort(data)
    
    # Output: [(1, 'c'), (1, 'd'), (2, 'f'), (3, 'a'), (3, 'e'), (4, 'b')]
    # Notice the order of equal elements is preserved: 'c' (index 1) comes before 'd' (index 3)
    # and 'a' (index 0) comes before 'e' (index 4).
    print(f"Sorted Data (Timsort - Stable): {data}")
    
    # Test case 2: Simple integer list
    data_int = [5, 21, 7, 23, 19, 3, 11, 40, 1]
    print(f"\nOriginal Integer List: {data_int}")
    timsort(data_int)
    print(f"Sorted Integer List: {data_int}")
