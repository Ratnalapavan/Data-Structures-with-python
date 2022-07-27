


if  __name__ == "__main__":
    arr = input("Please enter the array elements separated by space:").split()
    arr = [int(i) for i in arr]
    print("provided array is:\n{}".format(arr))
    len_arr = len(arr)
    for i in range(len_arr):
        min_ind = i
        for j in range(i,len_arr):
            if arr[min_ind] > arr[j]:
                min_ind = j
        temp = arr[i]
        arr[i] = arr[min_ind]
        arr[min_ind] = temp

    print("Sorted array after seletion sort is:\n{}".format(arr))