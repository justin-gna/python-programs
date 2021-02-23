# Problem J2: Time to Decompress from 2019
i = 0
j = 0
lines = int(input("enter the number of lines in the message: "))
newline = ["none"] * lines
while i < lines:
  newline[i] = input("enter line number " + str(i+1) + ": ") 
  i = i+1

while j < lines:
  print(int(newline[j][0]) * newline[j][2]) #indexing the string inside the list in order to retrieve the number values in newline[0] and multiply it by the character in newline[1] to display the proper output
  j = j + 1