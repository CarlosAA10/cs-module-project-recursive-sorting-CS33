# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # allocating all the memory for us from the start

    # Your code here
    a = 0
    b = 0

    # for i in range(len(merged_arr)):

    #     if arrA[a] < arrB[b]:
    #         merged_arr[i] = arrA[a]
    #         a += 1
    #     elif arrA[a] >= arrB[b]:
    #         merged_arr[i] = arrB[b]
    #         b += 1

    while a < len(arrA) and b < len(arrB):

        if arrA[a] < arrB[b]:

            merged_arr.append(arrA[a])
            a += 1
        else: 

            merged_arr.append(arrB[b])
            b += 1
        # at this point, we've merged in all of te elements from 
        # one of the arrays, but not the other

    # check both arrays to see if the pointer is still in range 
    # of its array 
    if a < len(arrA):
        # arrA still has leftover elements
        # push them all to the merged array
        merged_arr.extend(arrA[a:])

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr


arr1 = [13,76,90,89,456,432,53]
arr2 = [34,25,54,32,23]

print(merge(arr1,arr2))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # base case: stop splitting the arrays in half when the arrays reach a length of 1
    if len(arr) > 1:

        left = merge_sort(arr[0 : len(arr )// 2])
        right = merge_sort(arr[len(arr) // 2: ])

        arr = merge(left, right)

    return arr

# print(merge_sort(merge(arr1,arr2)))

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

