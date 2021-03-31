# Justin G. Fr. Michael Goetz CSS
# 3/30/2021
# A library of modules that can be used for sorting the grades of students by average, highest, lowest, or median marks

"""MERGE SORT FOR AVERAGE"""
### ------------------------------------------------------------------------------------ ###
def merge_avg(arr_a, arr_b):
  """A function that compares two values from two lists and returns a sorted list of two values"""

  arr_c = []

  # there should only be one value in both arr_a and arr_b so we check which average is lower (because we are sorting from low to high) and append it to arr_c 
  while len(arr_a) > 0 and len(arr_b) > 0:
    if arr_a[0].get_avg() < arr_b[0].get_avg():
      arr_c.append(arr_a[0])
      arr_a.pop(0)
    else:
      arr_c.append(arr_b[0])
      arr_b.pop(0)

  # either arr_a or arr_b is empty so we just append the remaining value from the list that is not empty
  while len(arr_a) > 0:
    arr_c.append(arr_a[0])
    arr_a.pop(0)

  while len(arr_b) > 0:
    arr_c.append(arr_b[0])
    arr_b.pop(0)

  return arr_c

def merge_sort_avg(arr):
  """A function that splits a list into two halves and keep splitting until each list has only one element and then returns a fully sorted list"""

  # base case for when the list has been split into lists with only one element in each
  if len(arr) == 1:
    return arr

  # splitting the list into two halves
  n = len(arr) - 1 
  arr_a = []
  arr_b = []
  for i in range(0, n//2 + 1):
    arr_a.append(arr[i])
  for j in range(n//2 + 1, n + 1):
    arr_b.append(arr[j])

  # recursively splitting the list until the lists contain just one element
  arr_a = merge_sort_avg(arr_a)
  arr_b = merge_sort_avg(arr_b)

  # when the lists are just one element we begin merging them into one whole sorted list
  return merge_avg(arr_a, arr_b)

'''functions below work the same as this one, (therefore they have no comments) but just sort based on highest, lowest, or median'''
### ==================================================================================== ###


"""MERGE SORT FOR HIGHEST"""
### ------------------------------------------------------------------------------------ ###
def merge_highest(arr_a, arr_b):
  arr_c = []

  while len(arr_a) > 0 and len(arr_b) > 0:
    if arr_a[0].get_highest() < arr_b[0].get_highest():
      arr_c.append(arr_a[0])
      arr_a.pop(0)
    else:
      arr_c.append(arr_b[0])
      arr_b.pop(0)

  while len(arr_a) > 0:
    arr_c.append(arr_a[0])
    arr_a.pop(0)

  while len(arr_b) > 0:
    arr_c.append(arr_b[0])
    arr_b.pop(0)

  return arr_c

def merge_sort_highest(arr):
  if len(arr) == 1:
    return arr

  n = len(arr) - 1 
  arr_a = []
  arr_b = []
  for i in range(0, n//2 + 1):
    arr_a.append(arr[i])
  for j in range(n//2 + 1, n + 1):
    arr_b.append(arr[j])

  arr_a = merge_sort_highest(arr_a)
  arr_b = merge_sort_highest(arr_b)

  return merge_highest(arr_a, arr_b)
### ==================================================================================== ###


"""MERGE SORT FOR LOWEST"""
### ------------------------------------------------------------------------------------ ###
def merge_lowest(arr_a, arr_b):
  arr_c = []

  while len(arr_a) > 0 and len(arr_b) > 0:
    if arr_a[0].get_lowest() < arr_b[0].get_lowest():
      arr_c.append(arr_a[0])
      arr_a.pop(0)
    else:
      arr_c.append(arr_b[0])
      arr_b.pop(0)

  while len(arr_a) > 0:
    arr_c.append(arr_a[0])
    arr_a.pop(0)

  while len(arr_b) > 0:
    arr_c.append(arr_b[0])
    arr_b.pop(0)

  return arr_c

def merge_sort_lowest(arr):
  if len(arr) == 1:
    return arr

  n = len(arr) - 1 
  arr_a = []
  arr_b = []
  for i in range(0, n//2 + 1):
    arr_a.append(arr[i])
  for j in range(n//2 + 1, n + 1):
    arr_b.append(arr[j])

  arr_a = merge_sort_lowest(arr_a)
  arr_b = merge_sort_lowest(arr_b)

  return merge_lowest(arr_a, arr_b)
### ==================================================================================== ###


"""MERGE SORT FOR MEDIAN"""
### ------------------------------------------------------------------------------------ ###
def merge_median(arr_a, arr_b):
  arr_c = []

  while len(arr_a) > 0 and len(arr_b) > 0:
    if arr_a[0].get_median() < arr_b[0].get_median():
      arr_c.append(arr_a[0])
      arr_a.pop(0)
    else:
      arr_c.append(arr_b[0])
      arr_b.pop(0)

  while len(arr_a) > 0:
    arr_c.append(arr_a[0])
    arr_a.pop(0)

  while len(arr_b) > 0:
    arr_c.append(arr_b[0])
    arr_b.pop(0)

  return arr_c


def merge_sort_median(arr):
  if len(arr) == 1:
    return arr

  n = len(arr) - 1 
  arr_a = []
  arr_b = []
  for i in range(0, n//2 + 1):
    arr_a.append(arr[i])
  for j in range(n//2 + 1, n + 1):
    arr_b.append(arr[j])

  arr_a = merge_sort_median(arr_a)
  arr_b = merge_sort_median(arr_b)

  return merge_median(arr_a, arr_b)
### ==================================================================================== ###
