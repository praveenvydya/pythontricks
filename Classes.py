students=[]

class Student:
    school_name="kakathiya"

    def __init__(self,name,rollno=22):
       self.name=name
       self.rollno = rollno
       #student  = {"name":name,"rollno":rollno}
       students.append(self)

    def __str__(self):
        return "Student"+self.name

    def _get_name_capitalize(self):
        return self.name.capitalize()

    def _get_school_name(self):
        return self.school_name


class HighSchoolData(Student):
    school_name = "Teddy Kids"

    def get_school_name(self):
        #return "High school student"
        return super()._get_name_capitalize()

    def get_name_capitalize(self):
        org_val = super().school_name.capitalize()
        return org_val+"-HS"

""" fdas fdsa 
:param fasd fas 
 
"""

james = HighSchoolData("james")
print(james.get_school_name())