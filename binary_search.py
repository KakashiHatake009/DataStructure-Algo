def binary_search(numbers,target):
    """
    Returns the index position of the target if found based on binary search algorithm, else returns None
    """
    lower_bound = 0
    upper_bound = len(numbers)-1
    while lower_bound <=upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        if numbers[midpoint] == target:
            return midpoint
        elif numbers[midpoint] < target:
            lower_bound = midpoint + 1
        else:
            upper_bound = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index using binary search: {index}")
    else:
        print("Target not found.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 10)
verify(result)
