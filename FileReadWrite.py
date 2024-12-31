import student

class TestStudent(St):

    def save_file(students):
        try:
            f = open("students.txt","a")
            for st in students:
                f.write(st+"\n")
                f.close()
        except Exception:
            print("unable to write file")


    print("Hello ")