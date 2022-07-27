
if __name__ == "__main__":
    arr = input("Please enter the array elements separated by space:").split()
    arr = [int(i) for i in arr]
    print("Provided array is:\n{}".format(arr))
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(i+1,len_arr):
            if arr[i] > arr[j]:
                temp  = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print("Sorted array after Bubble sort is:\n{}".format(arr))