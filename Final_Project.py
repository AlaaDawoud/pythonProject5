class Course:
    count=1
    def __init__(self,course_name,course_level):
        self.course_id = Course.count
        Course.count += 1
        self.course_name=course_name
        self.course_level=course_level

class Student:
    count =1
    def __init__(self,student_name,student_level):
        self.student_id = Student.count
        Student.count += 1
        self.student_name=student_name
        self.student_level=student_level
        self.student_courses=[]

    def add_new_course(self,course):
        if self.student_level==course.course_level:
            self.student_courses.append(course.course_name)
            print("The course has been added successfully to student")
        else:
            print(f"the course: {course.course_name} is not the same level with the student: {self.student_name}.")
    def display_student_details(self):
        name=self.student_name
        level=self.student_level
        courses=self.student_courses
        print(f"name of the student: {name}\nlevel of the student: {level}\n courses of the student: {courses}")

students=[]
courses=[]
while (True):
    x=int(input("Select Choice Please\n1.Add New Student\n2.Remove Student\n"
      "3.Edit Student\n4.Display All Students\n5.Create New Course\n6.Add course to student\n0.Exit\n"))
    if x==1:
        student_name=input("Enter student name: ")
        while (True):
            student_level=input("Enter student level (A-B-C): ")
            student_level=student_level.upper()
            if(student_level=='A' or student_level=='B' or student_level=='C'):
                student=Student(student_name,student_level)
                students.append(student)
                print("student saved successfully")
                break
    elif x==2:
        id=int(input("Enter student_id that you want to remove him: "))
        a1=True
        for i in students:
            if i.student_id == id:
                students.remove(i)
                print("delete done successful")
                a1=False
        if a1==True:
            print("user not exist")

    elif x==3:
        id = int(input("Enter student_id that you want to edit him: "))
        a2=True
        for i in students:
            if i.student_id == id:
                student_name = input("Enter new name: ")
                while (True):
                    student_level = input("Enter new student level (A-B-C): ")
                    student_level = student_level.upper()
                    if (student_level == 'A' or student_level == 'B' or student_level == 'C'):
                        i.student_name = student_name
                        i.student_level = student_level
                        print("Edit done successfully.")
                        a2=False
                        break
        if a2==True:
            print("user not exist")

    elif x==4:
        if students:
            print("All Students:\n")
            for i in students:
                i.display_student_details()
        else:
            print("No students found.")

    elif x==5:
        course_name = input("Enter course name: ")
        while (True):
            course_level = input("Enter course level (A-B-C): ")
            course_level = course_level.upper()
            if (course_level == 'A' or course_level == 'B' or course_level == 'C'):
                course = Course(course_name, course_level)
                courses.append(course)
                print("course saved successfully")
                break

    elif x==6:
        a3=True
        student_id=int(input("Enter student_id: "))
        for i in students:
            if i.student_id ==student_id:
                a3=False
                course_id=int(input("Enter course_id: "))
                a4=True
                for c in courses:
                    if c.course_id==course_id:
                        a4=False
                        i.add_new_course(c)
                if a4==True:
                    print("Course not exist")
        if a3==True:
            print("user not exist")

    elif x==0:
        break






