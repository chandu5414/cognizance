'''Write a python program to make a 2-dimensional list that contains represents a table of records, for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks.
'''
n=int(input('Enter the number of students : '))
a=[['Roll No','Name','Marks']]
for i in range(n):
    roll=input('Enter Roll No : ')
    studentname=input('Enter Student Name : ')
    marks=int(input('Enter Marks : '))
    a.append([roll,studentname,marks])
for i in range(len(a)):
    for j in range(len(a[i])):
        k=a[i][j]
        print(k,end='\t')
    print('\n')
h=int(input('Enter the row that should be printed : '))
for i in a[h]:
    print(i,end='\t')
