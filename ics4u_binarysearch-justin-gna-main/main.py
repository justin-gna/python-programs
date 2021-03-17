# Justin G. Fr. Michael Goetz CSS
# 3/3/2021
# A program that conducts a binary search on a list 

from random import randint

# Implement binary search here
def binary_search(arr, item):
  arr.sort()
  start = 0
  # end = len(arr) - 1 because we need the index
  end = len(arr) - 1
  mid = end // 2
  i = 0
  while i == 0:
    # when the start, mid and end are the same but the item is not the mid then it has checked the maximum amount of times without having found the item in the list
    if start == mid and start == end and item != arr[mid]:
      return False


    if item == arr[mid]:
      return True, mid

    # when the item is not the same as the mid, then we need to set new values for the start, mid and end before the next check
    elif item < arr[mid]:
      end = mid - 1
      mid = end // 2
  
    elif item > arr[mid]:
      start = mid + 1
      mid = start + ((end - start) // 2)
      
# declaring a random list and a random item in range of 1-10
arr = []
item = randint(1, 10)
for i in range(10):
  arr.append(randint(1, 10))

#output
arr.sort()
print(arr)
print(item)
print(binary_search(arr, item))

# resources:
# https://www.geeksforgeeks.org/binary-search/