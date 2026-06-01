import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Loading Data
# ----------------------------
#loading the student data from a csv file
df_students = pd.read_csv('student.csv')
#showing the student data
print(df_students)

#Student from each country
students_per_country = df_students['country'].value_counts()
print(students_per_country)

#Student from each program
students_per_program = df_students['program'].value_counts()
print(students_per_program)

#Average GPA per program
avg_gpa_per_program = df_students.groupby('program')['gpa'].mean()
print(avg_gpa_per_program)

#Highest GPA student
print(df_students[df_students['gpa'] == df_students['gpa'].max()])


#most numerous semester
most_numerous_semester = df_students['semester'].value_counts().idxmax()
print(most_numerous_semester)

#maximum student per semester
max_students_per_semester = df_students['semester'].value_counts().max()
print(max_students_per_semester)

#semester with equal number of students
equal_students_semester = df_students['semester'].value_counts()
equal_max_students_semester = equal_students_semester[equal_students_semester == max_students_per_semester]
print(equal_max_students_semester)

#null values in the dataset
print(df_students.isnull().sum())

#------------------------------
#plotting seperately the students per country, program and GPA distribution
#students per country
#plt.figure(figsize=(10, 6))
#students_per_country.plot(kind='bar')
#plt.title('Number of Students per Country')
#plt.xlabel('Country')
#plt.ylabel('Number of Students')
#plt.show()

#students per program
#plt.figure(figsize=(10, 6))
#students_per_program.plot(kind='bar')
#plt.title('Number of Students per Program')
#plt.xlabel('program')
#plt.ylabel('number of students')
#plt.show()

#GPA distribution
#plt.figure(figsize=(10, 6))
#df_students['gpa'].plot(kind='hist', bins=10)   
#plt.title('GPA Distribution')
#plt.xlabel('GPA')
#plt.ylabel('Frequency')
#plt.show()

#subplotting students per country and program and GPA distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
students_per_country.plot(kind='bar')
plt.title('Number of Students per Country')
plt.xlabel('Country')
plt.ylabel('Number of Students')
plt.xticks(rotation=90)
plt.subplot(1, 3, 2)
students_per_program.plot(kind='bar')
plt.title('Number of Students per Program')
plt.xlabel('Program')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.subplot(1, 3, 3)
df_students['gpa'].plot(kind='hist', bins=10)
plt.title('GPA Distribution')
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()






