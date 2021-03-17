[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4203737&assignment_repo_type=AssignmentRepo)
# ICS3U4U_Lists

Your task is to write a program that asks for a bunch of stings, then allows the user to interactively ask for details about his/her list.

## Grade ICS4U Initial Input
First, the user will be asked for a number.. how many elements will be in the list.
Then the user will be prompted that many times to input something, then that thing will be appended to the list.
As the user is inputting elements, if the element consists of only digits, then cast that element to an integer. If the element is a boolean (CHeck if the string is equal to "True" or "False" then append the actual boolean value to the list.

## Grade ICS3U Initial Input
The user will be asked to input a list as follows:
```
>> Please Enter a list: [1,2,3,4,"hello",5,6,"milk"]
```
Then you can convert it into a list as follows
```
list_of_items = input("Please enter a list: ")
# Note: eval is EVIL. I'm only using it here to make things easier.. but ideally, in a real life program, this would be accomplished in a similar way to how I'm having the ICS4U crowd do it... food for thought
list_of_items = eval(list_of_items)
```

## Program Execution
Once the list has been entered, the user will have a choice to enter one of 5 possible values:
```
length
first
last
range
sort
```

Given any of these commands, the program should output the appropriate data. 

Note that if the user types "range" you will need another set of inputs to get the start and end of the range.

Note on sorting: 
1. You need to use the ```sorted()``` function so as to not ruin the first and last calls.
2. Call sorted like this: ```sorted(list_of_items, key=str)```. Trust me. Otherwise you'll get an error saying it does'nt know how to use '<' on ints and strs.

## Interactivity
To ensure this program is interactive, we will throw our code in a while loop so that the user can keep asking questions about his/her list until he types "done"

The main.py includes a skeliton for this interaction, so you only need to code the above problem.

## Example Execution of Code (ICS4U)
```
>>> Now many items? 4
Milk
Bread
2
Pineapple Pizza

Enter a command: first
Milk

Enter a command: length
4

Enter a command: sort
[2, 'Bread', 'Milk', 'Pineapple Pizza']

Enter a command: range
Sart: 1
End: 3
['Bread', 2]

Enter a command: done
```

## Example Execution of Code (ICS3U)
```
>>> Enter a list of items: ['Milk', 'Bread', 2, 'Pineapple Pizza']

Enter a command: first
Milk

Enter a command: length
4

Enter a command: sort
[2, 'Bread', 'Milk', 'Pineapple Pizza']

Enter a command: range
Sart: 1
End: 3
['Bread', 2]

Enter a command: done
```
