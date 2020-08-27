no_of_leaves = 8

    def __init__(self, e_name, e_salary, e_department, e_role):

        self.name = e_name
        self.salary = e_salary
        self.department = e_department
        self.role = e_role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}, Department is {self.department} and role is {self.role}"

    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leaves = newleaves



sabbir = Employee("Sabbir Ahamed", 1800, "IT", "Dev")
michael = Employee("Michael Horton", 2000, "IT", "Lead Dev")
Kelly = Employee("Kelly Joyane", 1300, "IT", "BA")

#Employee.no_of_leaves = 89

sabbir.change_leave(33)

print(sabbir.salary, sabbir.no_of_leaves)
print(michael.name, michael.salary, michael.department, michael.role, michael.no_of_leaves)
