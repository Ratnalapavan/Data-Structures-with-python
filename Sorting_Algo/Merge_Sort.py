
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        #diciding the array in halves
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #sorting the left part
        merge_sort(left_arr)
        #sorting the right part
        merge_sort(right_arr)

        i = j = k = 0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
            else:
                arr[k] = right_arr[j]
                j = j+1
            k = k+1

        #for left over elements in left_arr which are not added in main list with 'k' variable
        #consider 1 8 9 and 2 3 4 now 1 2 3 4 gets added via a[k] but j becomes equal to its length so above--
        #--while loop breaks leaves 8 9 in left array so below code is implemented
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1

        #for left over elements in right_arr which are not added in main list with 'k' variable
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1   

arr = input("Please enter the array elements separated by space:").split()
arr = [int(i) for i in arr]
print("provided array is:\n{}".format(arr))
merge_sort(arr)
print("Sorted array after seletion sort is:\n{}".format(arr))
