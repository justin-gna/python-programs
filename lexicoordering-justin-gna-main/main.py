# Justin G. Fr. Michael Goetz CSS
# 2/22/2021
# Lexicographical Comparison Program: A program that will take in an input number and output a list of numbers in range of that number in lexicographical order

def make_list(num):
  num_list = []
  for i in range(1, num + 1):
    num_list.append(str(i))

  return num_list

def lexico_order(num):
  num_list = make_list(num)
  new_list = []
  # basically just goes through the list and adds all the things starting with '1' to the new_list first and then loops again for every number after 
  for number in num_list:
    if number[0] == '1':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '2':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '3':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '4':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '5':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '6':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '7':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '8':
      new_list.append(int(number))

  for number in num_list:
    if number[0] == '9':
      new_list.append(int(number))

      
  return new_list

num = int(input("enter a number: "))
print(lexico_order(num))

# i admit this was a pretty crude way to accomplish the goal but it was the simplest thing i could think of