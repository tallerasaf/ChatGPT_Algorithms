from typing import List


# Constants
NUMBER_LIST = [10, 4, 5, 8, 6, 11, 26]
LEFT_INDEX = 0
CHUNK_SIZE = 5


# Quickselect Algorithm
def quick_select(numbers: List[int], k: int) -> int:
    if len(numbers) <= CHUNK_SIZE:
        return sorted(numbers)[k]

    # Divide and conquer using median of medians
    pivot_index = median_of_medians(numbers, k)
    pivot_index = partition(numbers, 0, len(numbers) - 1, pivot_index)

    # Recurse on the appropriate sub-list
    if k == pivot_index:
        return numbers[k]
    elif k < pivot_index:
        return quick_select(numbers[:pivot_index], k)
    else:
        return quick_select(numbers[pivot_index + 1:], k - pivot_index - 1)


# Median of Medians Algorithm
def median_of_medians(numbers: List[int], k: int) -> int:
    if len(numbers) <= CHUNK_SIZE:
        return sorted(numbers)[k]

    # Divide the input into chunks and recursively find the median of each chunk
    chunks = [
        numbers[i:i + CHUNK_SIZE] 
        for i in range(LEFT_INDEX, len(numbers), CHUNK_SIZE)
    ]
    medians = [median_of_medians(chunk, len(chunk) // 2) for chunk in chunks]

    # Use quickselect to find the median of medians and return its index in the original list
    pivot = quick_select(medians, len(medians) // 2)
    return numbers.index(pivot)


# Partition Algorithm
def partition(numbers: List[int], left: int, right: int, pivot_index: int) -> int:
    pivot_value = numbers[pivot_index]

    # Move the pivot element to the end of the sublist
    numbers[pivot_index], numbers[right] = numbers[right], numbers[pivot_index]

    # Partition the sublist into elements smaller than and larger than the pivot value
    store_index = left
    for i in range(left, right):
        if numbers[i] < pivot_value:
            numbers[i], numbers[store_index] = numbers[store_index], numbers[i]
            store_index += 1

    # Move the pivot element to its final position and return its index
    numbers[right], numbers[store_index] = numbers[store_index], numbers[right]
    return store_index


# Test with main function
def main():
    k = 3
    result = quick_select(NUMBER_LIST, k - 1)
    print(f"The {k}-th smallest element in {NUMBER_LIST} is: {result}")


if __name__ == '__main__':
    main()
