def quick_sort(arr,low,high):
    if low < high:
        pivot_ind = partition(arr,low,high)
        quick_sort(arr,low,pivot_ind-1)
        quick_sort(arr,pivot_ind+1,high)

def partition(arr,low,high):
    i = low-1
    pivot =  arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

arr = input("Please enter the array elements separated by space:").split()
arr = [int(i) for i in arr]
print("provided array is:\n{}".format(arr))
quick_sort(arr,0,len(arr)-1)
print("Sorted array after Quick sort is:\n{}".format(arr))