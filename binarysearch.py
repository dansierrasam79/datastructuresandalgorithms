def binary_search(arr, target):
    """
    Performs a binary search to find the index of a target value in a sorted list.
    Time Complexity: O(log n)
    
    Args:
        arr (list): The sorted list (array) to search within.
        target (int/float/str): The value to search for.

    Returns:
        int: The index of the target if found, or -1 if the target is not present.
    """
    # Initialize the pointers for the search window
    low = 0
    high = len(arr) - 1

    # Continue searching as long as the window is valid (low <= high)
    while low <= high:
        # Calculate the middle index
        # Using integer division // and this formula prevents overflow on huge lists
        mid = low + (high - low) // 2
        
        # Check if the target is present at the middle
        if arr[mid] == target:
            return mid
        
        # If the target is greater than the middle element, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
            
        # If the target is smaller than the middle element, ignore the right half
        else:
            high = mid - 1
            
    # If the loop finishes, the target was not found
    return -1

# --- Example Usage ---
if __name__ == "__main__":
    
    # NOTE: Binary Search REQUIRES the list to be sorted for correctness
    sorted_data = [4, 8, 12, 15, 16, 23, 35, 42]
    
    print(f"Sorted data list: {sorted_data}")
    
    # Case 1: Target is present (in the middle)
    target_1 = 16
    index_1 = binary_search(sorted_data, target_1)
    
    if index_1 != -1:
        print(f"\nSearching for {target_1}: Found at index {index_1}.")
    else:
        print(f"\nSearching for {target_1}: Not found.")

    # Case 2: Target is the first element
    target_2 = 4
    index_2 = binary_search(sorted_data, target_2)
    
    if index_2 != -1:
        print(f"\nSearching for {target_2}: Found at index {index_2}.")
    else:
        print(f"\nSearching for {target_2}: Not found.")

    # Case 3: Target is the last element
    target_3 = 42
    index_3 = binary_search(sorted_data, target_3)
    
    if index_3 != -1:
        print(f"\nSearching for {target_3}: Found at index {index_3}.")
    else:
        print(f"Searching for {target_3}: Not found.")
        
    # Case 4: Target is not present
    target_4 = 50
    index_4 = binary_search(sorted_data, target_4)
    
    if index_4 != -1:
        print(f"\nSearching for {target_4}: Found at index {index_4}.")
    else:
        print(f"\nSearching for {target_4}: Not found.")
