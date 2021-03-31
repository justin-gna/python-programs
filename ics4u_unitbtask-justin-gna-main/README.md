[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4425033&assignment_repo_type=AssignmentRepo)
# ICS4U Unit B Task

## Assignment Task
Your job is essentially to read some data about student grades from a csv file, sort the data, and put the data into another csv file. But the HOW you are going to do that is the point of this assignment.

A file called mr-habib-solution.cpython-38.pyc has been included to see if your code produces the right stuff!

You will complete this task in the following way:
1. Define a class called **Student** that has the following attributes and place it in student.py
```python
name # Student's name
grades # List of grades
```
2. Create the following methods for the students:
```python
__init__(self, name, grades) # Constructor function to initialize the Student
get_avg(self) # Returns the student's average
get_highest(self) # Returns the student's highest mark
get_lowest(self) # Returns the student's lowest mark
get_median(self) # Returns the student's median* mark
```
\* [median](https://www.mathsisfun.com/median.html)

3. Read the data from the given csv file. For each row of the CSV file, create a **Student** object and append that student object to a list called **students**

4. Write a function that writes this array to a csv file called **sorted_grades.csv**

5. Write a function (in the main module) called **merge_sort_avg** that takes the students list as a parameter and returns a sorted list that is sorted on the students average (low to high).

6. Write a function called **merge_sort_highest** that takes the students list as a parameter and returns a sorted list that is sorted on the student's highest grade (low to high)

7. Repeat this for lowest and median.

8. Write a function called main() that is only called when \_\_name\_\_ == '\_\_main\_\_' that asks the user to input one of four options: average, highest, lowest, median. Your program will proceed to generate the student's list, sort it appropriately, and write that sorted list to the sorted_grades.csv

## Merge Sort
[Geeks for Geeks](https://www.geeksforgeeks.org/python-program-for-merge-sort/)
[Ask Python](https://www.askpython.com/python/examples/merge-sort-in-python)
Litterally google it!

## What am I testing here?
Lists, Sorting, Recursion, Modules, Classes

## Grading
You will be marked on your solution (out of 4), coding style (out of 2), and comments (out of 2)

