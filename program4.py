#wtp to read the employee data : name , age , designation,salary from user and display it( by using lists)
count = int(input("Enter the number of employees :"))
name_list = []
age_list = []
designation_list = []
salary_list = []
for i in range (0,count):
    name = input("Enter the name :")
    age = int(input("Enter the age :"))
    designation = input("Enter the Designation :")
    salary = int(input("Enter the salary amount :"))
    name_list.append(name)
    age_list.append(age)
    designation_list.append(designation)
    salary_list.append(salary)
    print(name_list)
    print(age_list)
    print(designation_list)
    print(salary_list)
