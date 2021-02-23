# Justin G. Fr. Michael Goetz CSS
# 2/18/2021
# Int Converter: A program that converts a user input (string) and converts it into a int data type. 

def my_int(user_string):
  numbers_list = []
  # checks if the letter is a number if it is then it adds it to any empty list 
  if '.' in user_string:
    where_to_strip = user_string.find('.')
    after_decimal = user_string[where_to_strip:]

    if not after_decimal.isdecimal():
      return None
    else:
      user_string = user_string[:where_to_strip]

  for char in user_string:
    if char.isdigit():
      numbers_list.append(char)
    else:
      return None
 
  # changes the list from strings into ints and copies the values to a new list
  numbers_int_list = []  
  for digit in numbers_list:
    if digit == '0':
      numbers_int_list.append(0)
    elif digit == '1':
      numbers_int_list.append(1)
    elif digit == '2':
      numbers_int_list.append(2)
    elif digit == '3':
      numbers_int_list.append(3)
    elif digit == '4':
      numbers_int_list.append(4)
    elif digit == '5':
      numbers_int_list.append(5)
    elif digit == '6':
      numbers_int_list.append(6)
    elif digit == '7':
      numbers_int_list.append(7)
    elif digit == '8':
      numbers_int_list.append(8)
    elif digit == '9':
      numbers_int_list.append(9)
    
  # multiplies the values in the list by the corresponding power of 10
  # Ex. if the number is 123 the loop will do:
  # 1 * 10^3-0-1 = 100 
  # 2 * 10^3-1-1 = 100 + 20
  # 3 * 10^3-2-1 = 100 + 20 + 3
  #              = 123 <class 'int'>
  number = 0
  for i in range(len(numbers_int_list)):
    number +=  numbers_int_list[i] * 10**(len(numbers_int_list) - i - 1)

  return number

user_string = input("input something: ")
user_number = my_int(user_string)

print(user_number, type(user_number))