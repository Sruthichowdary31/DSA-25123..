def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)

insertion_sort(arr)

print("Sorted array:", arr)
