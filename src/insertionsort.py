def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >=0 and arr[j]>key) :
            arr[j+1] = arr[j]
            print('arr: ', arr)
            j -= 1
            arr[j+1] = key
            print('arr2: ', arr)

arr = [90,64,33,100,11]
sort(arr)
print('Sorted array: ', arr)