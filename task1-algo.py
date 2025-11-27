def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

num = [70,30,80,10,50,20]
sorted_list = selection_sort(num)
print("Sorted list:", sorted_list)
