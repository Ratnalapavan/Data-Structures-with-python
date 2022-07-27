from re import L


if __name__ == "__main__":
    arr = input("Please enter the array elements separated by space:").split()
    arr = [int(i) for i in arr]
    print("provided array is:\n{}".format(arr))
    len_arr = len(arr)
    for i in range(1,len_arr):
        key = arr[i]
        j = i-1

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]     #changing next index with itself with the same value
            j -= 1            #condition to break loop when comparition reach 0 index
        
        arr[j+1] = key #swap the min index with key 

    print("Sorted array after Insertion sort is:\n{}".format(arr))