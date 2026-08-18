def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Divide the array
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # Merge the sorted parts
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Sorting
merge_sort(arr)

# Output
print("Sorted array:", arr)
