import json
student_id = 0
list = []

#Taking the data of student from the user.
def enter_data():
    globals()['student_id'] = globals()['student_id'] + 1
    std_id = globals()['student_id']
    std_id = int(input("enter student id"))
    first_name = input("please enter first name:")
    last_name = input("enter last name: ")
    school_name = input("enter school name: ")
    class_name = input("enter class name: ")
    marks = int(input("enter marks: "))

    dict = {"student_id":std_id,
    "first_name":first_name,
    "last_name":last_name,
    "school_name":school_name,
    "class_name":class_name,
    "marks":marks,
    }
    list.append(dict)

#Storing the data in the file.
def writefile(list):
    with open('Data.json','w') as f:
        json.dump(list, f)
        f.write('\n')

#reading the data from file
def read(student_id):
    with open('Data.json','r') as f:
        data = json.load(f.read())
    std_id = int(input("please enter the id\n"))
    for data in Data:
        if Data['student_id'] == std_id:
            print(Data)
            

enter_data()
writefile(list)



         