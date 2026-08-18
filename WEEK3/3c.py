def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)

selection_sort(arr)

print("Sorted array:", arr)
