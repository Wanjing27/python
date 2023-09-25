name=input("name of the employee")
number=input("ID number: ")
depart=input('department: ')
job=("job title: ")

class Employee:
    def __init__(self,n,i,d,jt):
        self.name=n
        self.number=i
        self.department=d
        self.job=jt

    def __str__(self):
        return(self.name)
