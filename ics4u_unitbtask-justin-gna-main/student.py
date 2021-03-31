# Justin G. Fr. Michael Goetz CSS
# 3/24/2021
# A program that takes in the names of students and their grades and creates an object with that information using the class Student()
import csv

class Student():
  """A class that takes in a student's name and grades and creates an object which can be accessed to find the student's average, highest, lowest, or median marks"""

  def __init__(self, name, grades):
    """Initialization of the Student class by taking in the student name and a list of grades"""
    self._name = name
    self._grades = grades
    # this list is created so that writing to .csv files easier
    self._csv = []
    self._csv.append(name)
    for grade in grades:
      self._csv.append(grade)
 
  # def __str__(self):
  #   return f"{self._name} {self._grades}"

  def get_avg(self):
    """Gets the average of the student's grades"""
    int_grades = []
    for grade in self._grades:
      int_grades.append(int(grade))
    avg = (sum(int_grades)) / len(self._grades)
    # print(f"{self._name}'s average is approximately {round(avg, 2)}")
    return avg

  def get_highest(self):
    """Gets the student's highest grade"""
    highest = 0
    for grade in self._grades:
      if int(grade) > highest:
        highest = int(grade)
    # print(f"{self._name}'s highest grade is {highest}")
    return highest
  
  def get_lowest(self):
    """Gets the student's lowest grade"""
    lowest = 100
    for grade in self._grades:
      if int(grade) < lowest:
        lowest = int(grade)
    # print(f"{self._name}'s lowest grade is {lowest}")
    return lowest

  def get_median(self):
    """Gets the student's median grade"""
    mid = (len(self._grades) - 1) // 2
    int_grades = []
    for grade in self._grades:
      int_grades.append(int(grade))
    sorted_list = sorted(int_grades)
    # print(f"{self._name}'s median grade is {sorted(self._grades)[mid]}")
    return sorted_list[mid]

if __name__ == '__main__':
  with open('student_grades.csv', 'r') as in_file:
    text = csv.reader(in_file)

    student_names = []
    student_grades = []
    for line in text:
      student_names.append(line[0])
      line.pop(0)
      student_grades.append(line)

  students = []
  for i in range(len(student_names)):
    students.append(Student(student_names[i], student_grades[i]))

  print(students[6].get_median())
