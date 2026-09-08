Students = [{'id': 1, 'name': 'pri', 'age': 22, 'city': 'Pune'},{'id': 2, 'name': 'Priyal', 'age': 22, 'city': 'Pune'}]
"""
def addStudent():

    student_id = int(input("Students id : "))
    name = input("Enter students name : ")
    age = int(input("Enter students age: "))
    city = input("Enter students city : ")

    student = {"id":student_id, "name":name,"age":age,"city":city}
    Students.append(student)

addStudent()    
print(Students)"""
"""
def readStudent():

    for student in Students:

        print(f"id : {student["id"]}")
        print(f"Student name : {student["name"]}")
        print(f"age : {student["age"]}")
        print(f"city : {student["city"]}")
        print()

readStudent()"""
"""
def updateStudent():

    id = int(input("Enter id"))


    for student in Students:

        if id == student["id"]:

            student["name"] = input("Enter name :")
            student["age"] = input("Enter age : ")
            student["city"] = input("Enter city : ")


    print("Updated Sucessfully!!!")

updateStudent()

print(Students)
"""


def deleteStudent():

    id = int(input("Enter student id : "))

    for student in Students:
        if id == student["id"]:

            Students.remove(student)

    print("deleted sucessfully ....")


deleteStudent()

print(Students)