# Problem S3: Searching for Strings from 2020
original_string = input()
read_string = input()
count = 0

# ngl i dont really understand what this exactly does other than it gets the permutations of the original_string and stores them in the list perms
from itertools import permutations
perms = [''.join(p) for p in permutations(original_string)]

# stores the permutations into a set so there are no duplicates and then stores it back into the list so that it can be indexed
perms_set = set(perms)
perms = list(perms_set)

# loop to compare the substrings of read_string to the permutations of original_string
i = 0
j = 0
appears = False
while i < (len(perms)):
  if appears == True:
    count = count + 1
    j = 0
    appears = False
  elif perms[i][j] == read_string[i + j]:
      j = j + 1
      if j >= (len(original_string) - 1):
        appears = True
        j = 0
        i = i + 1
  else:
    j = j + 1
    if j >= (len(original_string) - 1):
      appears = False
      j = 0
      i = i + 1

print(count)

# time, 11:42 PM, i finally figured out how to do it like 2 and a half hours ago but it took me until now to get it working properly (onlt works like half the time tho, hopefully i'll learn why and how to fix it), and all i had to do was delete like 1 line of code. i kinda hate how stupidly long this took but it was cool to do either way. Hopefully you don't enter a "original_string" that is longer than 3 bc like it'll probably take a while since i brute forced it to find all the permutations. Anyways thank you and good night, or morning i guess since you'll see this tomorrow 