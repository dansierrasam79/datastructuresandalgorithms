def linear_search(arr, target):
    """
    Performs a linear search to find the index of a target value in a list.
    Time Complexity: O(n)

    Args:
        arr (list): The list (array) to search within.
        target (int/float/str): The value to search for.

    Returns:
        int: The index of the target if found, or -1 if the target is not present.
    """
    # Iterate through the list from the beginning to the end
    for i in range(len(arr)):
        # Check if the current element matches the target
        if arr[i] == target:
            # If a match is found, return its index immediately
            return i
    
    # If the loop finishes without finding the target, return -1
    return -1

# --- Example Usage ---
if __name__ == "__main__":
    
    data = [42, 15, 8, 23, 16, 4, 35, 12]
    
    print(f"Data list: {data}")
    
    # Case 1: Target is present
    target_1 = 16
    index_1 = linear_search(data, target_1)
    
    if index_1 != -1:
        print(f"\nSearching for {target_1}: Found at index {index_1}.")
    else:
        print(f"\nSearching for {target_1}: Not found.")

    # Case 2: Target is the first element
    target_2 = 42
    index_2 = linear_search(data, target_2)
    
    if index_2 != -1:
        print(f"\nSearching for {target_2}: Found at index {index_2}.")
    else:
        print(f"\nSearching for {target_2}: Not found.")

    # Case 3: Target is not present
    target_3 = 100
    index_3 = linear_search(data, target_3)
    
    if index_3 != -1:
        print(f"\nSearching for {target_3}: Found at index {index_3}.")
    else:
        print(f"\nSearching for {target_3}: Not found.")

    # Case 4: Target using strings
    data_str = ["apple", "banana", "cherry", "date"]
    target_4 = "cherry"
    index_4 = linear_search(data_str, target_4)

    print(f"\nString list: {data_str}")
    if index_4 != -1:
        print(f"Searching for {target_4}: Found at index {index_4}.")
    else:
        print(f"Searching for {target_4}: Not found.")
