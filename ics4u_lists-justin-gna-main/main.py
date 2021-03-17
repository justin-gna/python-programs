# Justin G. Fr. Michael Goetz CSS
# 2/25/2021
# Lists: A program that asks the user to enter a list and then lets them inspect it with different commands

# Enter the contents of the list here
list_size = int(input("enter how many items you would like your list to hold: "))
user_list = []
for i in range(list_size):
  # prompt to enter the next item in the list
  user_input = (input("enter list item " + str(i + 1) + ": "))

  # checks if the striing can be parsed to a different data type and if it can it does so and appends that new value to the list otherwise it will append the input as a string
  if user_input.isdigit():
    user_input = int(user_input)
  elif '-' in user_input and not user_input.islower() and not user_input.isupper():
    user_input = int(user_input) 
  elif user_input == 'True':
    user_input = True
  elif user_input == 'False':
    user_input = False
  user_list.append(user_input)

# list of commands that the user can use on their inputted list
print("\nthe following is a list of commands:\nlength: (shows the length of the list)\nfirst: (shows the first item in the list)\nlast: (shows the last item in the list)\nrange: (select a range of items in the list to display, ex. 1 to 2)\nsort: (show the list in a sorted order)\ndone: (closes the program, therefore resetting all data)\n")

user_command = 'none'
# Use strip and lower to ensure that no matter how the user types in done (Eg. "  DonE") it will finish
while user_command.strip().lower() != 'done':
  # Process the response assuming the user did not enter 'done', and carries out the corresponding command based on the input
  user_command = input("enter what you want to do with the list: ")
  if user_command.strip().lower() == 'length':
    print(list_size)
  elif user_command.strip().lower() == 'first':
    print(user_list[0])
  elif user_command.strip().lower() == 'last':
    print(user_list[-1])
  elif user_command.strip().lower() == 'range':
    range_start = int(input("start of range: "))
    range_end = int(input("end of range: "))
    print(user_list[range_start:range_end])
  elif user_command.strip().lower() == 'sort':
    print(sorted(user_list, key=str))
  elif user_command.strip().lower() != 'done':
    print("invalid input, if you want to exit enter 'done'")
