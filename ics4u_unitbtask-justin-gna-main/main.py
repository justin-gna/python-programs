# Justin G. Fr. Michael Goetz CSS
# 3/30/2021
# A program that reads and stores the names and grades of students from a .csv file. then sorts those students by either average, highest, lowest, or median marks with merge_sort(), and then writes the ordered students to a new .csv file.

def main():
  
  import sort
  from student import Student
  import csv

  with open('student_grades.csv', 'r') as in_file:
    text = csv.reader(in_file)

    # 1D list for student names and 2D list for student grades
    student_names = []
    student_grades = []
    for line in text:
      # the values are appended this way because the first value in every line is the name and everything after is the grades
      student_names.append(line[0])
      line.pop(0)
      student_grades.append(line)

  # creating the students list of objects with the imported class Student()
  students = []
  for i in range(len(student_names)):
    students.append(Student(student_names[i], student_grades[i]))


  print("sorting commands: 'average', 'highest', 'lowest' or 'median'")
  command = input("How would you like to sort the students? ")
  with open('sorted_grades.csv', 'w') as out_file:
    csvwriter = csv.writer(out_file)

    # written this way because the first object in the students list is the format "Name,A0,A1..." so that is written first and a new list without the first object to avoid the error of trying to interpret A0,A1... as actual numbers
    csvwriter.writerow(students[0]._csv)
    new_list = students
    new_list.pop(0)

    if command.lower() == "average":
      for obj in sort.merge_sort_avg(new_list):
        csvwriter.writerow(obj._csv)

    elif command.lower() == "highest":
      for obj in sort.merge_sort_highest(new_list):
        csvwriter.writerow(obj._csv)

    elif command.lower() == "lowest":
      for obj in sort.merge_sort_lowest(new_list):
        csvwriter.writerow(obj._csv)
    
    elif command.lower() == "median":
      for obj in sort.merge_sort_median(new_list):
        csvwriter.writerow(obj._csv)

    else:
      print("invalid command")
      print("can only sort by: 'average', 'highest', 'lowest' or 'median'")
  

if __name__ == '__main__':
  main()


# references:
# https://docs.python.org/3/library/csv.html#csv.writer
# https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/?ref=rp
# https://youtu.be/4VqmGXwpLqc