students =[]
class Student:
    def __init__(self,name):
        self.name = name
        students.append(self)
    def get_students(self):
        return students

    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student.title()
        return students_titlecase

    students_list  = get_students_titlecase()

    def var_args(name,*args):
        print(name,args)

   # var_args("praveen",1,"Hi",True)

class TestStudent(Student):

    def save_file(students):
        try:
            f = open("students.txt","a")

            f.write(students+"\n")

            f.close()
        except Exception:
            print("unable to write file")

    def read_file():
        try:
            f= open("students.txt","r")
            for st in f.readline():
                print(st)
            f.close()
        except Exception:
            print("unable to read file")

print("Hello ")
Student("Praveen")
Student("mounika")
st =Student("Meena")
Student.
students = st.get_students()

TestStudent.save_file("students")
TestStudent.read_file()



