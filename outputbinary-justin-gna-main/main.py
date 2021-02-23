# Justin G. Fr. Michael Goetz CSS
# 2/23/2021
# Binary Encoder: A program that takes text input from a file and translates the text into binary and writes it to a new file

with open('input.txt', 'r') as in_file:
  with open('output.bin', 'wb') as out_file:

    # reads from the input file and adds all the text to a string and replaces the \n characters with just spaces because i dont think there is a binary value for \n
    text = in_file.read().replace('\n', ' ')

    # gets the ascii value for every letter/char in the text and then converts it into binary code and then writes the byte to a output binary file
    for letter in text:
      letter_ord = ord(letter)
      binary_byte = f"{letter_ord:08b}".encode()
      out_file.write(binary_byte)