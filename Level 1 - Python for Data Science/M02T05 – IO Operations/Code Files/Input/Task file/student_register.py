# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 10:02:57 2025

@author: juleigar
"""

#Need to create a student register
#Requires input from user to determine number of students
#write the file with the ids to an output file

total_students = int(input("Enter total number for registered students: "))
students= [] # 1D list

#loop through inputs and ad to student list
for i in range(0,total_students):
    if i <=total_students:
        student_id = input("Students ID: ")+"................"
        students.append(student_id)
      
    else:
        break

#write to file
with open("reg_form.txt", "w") as f:
        #loop through the list and write each element as a separate line
        for student in students:
            f.write(student+"\n")
            print(student)



