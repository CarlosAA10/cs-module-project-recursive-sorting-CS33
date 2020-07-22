# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # if you wrote this in a recursive call
    # start = 0
    # end = len(arr) -1
    # it would not work since you would be setting your variables back to the same each time you recursed
    # this gives us a clue that we can update it on the recursive call so we do that below

    if start > end:
        return -1

    # how do we move closer to a base case
    # we'll stop when we either find te target or if we've traversed 
    else:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
            return binary_search(arr, target, start, end)
        else:
            end = mid - 1
            return binary_search(arr, target, start, end)

    
arr = [1,2,3,4,5,6,78,90,111]
print(binary_search(arr, 111, 0, len(arr) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here


# # def find_pos(a 
# # )