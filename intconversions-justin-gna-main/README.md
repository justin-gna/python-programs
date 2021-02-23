[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4157955&assignment_repo_type=AssignmentRepo)
# ICS4U-IntConversion

The original python int() function is great, but it has some shortcomings.
One shortcoming is that your entire program will crash if you give it a string that contains non-numeric characters.
Another one is that if you want to convert "12.34" to a string, int() will cause an error... wouldn't it make more sense for it to just return the int portion, namely, 12?

Well,your job is to create a function called ```my_int()```that takes a variable of type 'str' as a parameter and returns an integer with the value in the string.
If the string contains any characters that are not a number (except a period for a decimal), simply return ```None```

**NOTE: You may not use the int() function within your implementation!**

## Example Input
"123"

## Example Output
123

## Example Input 2
"123.56"

## Example Output 2
123

## Example Input 3
"123Hello"

## Example Output 3
None

Some things you may find helpful:
To define a function call my_int that takes a string as a parameter:

```
def my_int(input_string):
  # do something with input_string
  ...
```
 
You may want to go through the string character by character and convert that way, but I'll leave the implementation up to you guys.
 
