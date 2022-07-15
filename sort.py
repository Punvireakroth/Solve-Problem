# def bubbleSort(arr):
#     n = len(arr)
  
#     # Traverse through all array elements
#     for i in range(n):
  
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
  
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
  
  
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
  
# bubbleSort(arr)
  
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i], end=" ")



# --------------------------------------------------------
# def sortList(arr):
#     for i in range(len(arr)):
#         for j in range((len(arr) - i) - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [1, 5, 2, 9, 7, 8, 0]

# sortList(arr)

# for i in range(len(arr)):
#     print("%d" % arr[i], end=" ")

#----------------------------------------------------------

# list = [1,3,5,3,6,8,23,64,9,10]
# new_list = []
# while list:
#     maximum = list[0]
#     for i in list:
#         if maximum < i: 
#            maximum = i

#     new_list.append(maximum)
#     list.remove(maximum)
# print(new_list)

#----------------------------------------------------------

# Gien a array arr[] of n element, write a Python function to seach a given element x in arr[]
what_user_want = int(input("What number so wanna search? "))
print('----------------------------------------')

def search(number):
    arr = [1,3,5,3,6,8,23,64,9,10]
    for i in arr:
        if(i == what_user_want):
            flag = True
    if flag:
        print(f"Your number is at index {arr.index(what_user_want)}")
        return True
    else:
        print(f"Your number is not on the list")
        return False

answer = search(what_user_want)
print(answer)