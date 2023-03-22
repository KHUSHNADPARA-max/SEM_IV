def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = [int(input("Enter a number: ")) for _ in range(10)]
print("Before sorting:", arr)

sorted_arr = quick_sort(arr)

print("After sorting:", sorted_arr)
