students = {}

def diet_plan(student_name):
    if student_name not in students.keys():
        print("Student not found")
    else:
        in1 = [int(i) for i in input("Enter agility and speed seperated by commas : ").split(",")]
        factors = students[student_name]["factors"]
        print("Printing the details of the student")
        print(students[student_name])
        print("Diet plans is as follows")
        if(factors[0] < in1[0]):
            print("For agility : Needs to work on strength hence green vegetables and high protien food is preferred")
        else:
            print("For agility : Over consumption is there so balance the diet and limit the protien intake")
        if(factors[2] < in1[1]):
            print("For speed: Workout should be increased, high protien food is required")
        else:
            print("For speed: Yuor diet is fair enough just balnce your diet more")
            
def add_student(name, weight, height, sport):
    
    if name not in students.keys():
        factors = []
        if sport.lower() == 'cricket':
            factors = [10, "Average", 12]
        if sport.lower() == 'javlin':
            factors = [15, "High", 8]
        if sport.lower() == 'chess':
            factors = [15, 'Low', 5]
        if sport.lower() == 'football':
            factors = [12, 'High', 14]
            
        students[name] = {
            "weight" : weight,
            "height" : height,
            "preferred_sport" : sport
        }
        students[name]["factors"] = []
        students[name]["factors"] = factors
        print(students)
    else:
        print("Student already exists")



            
print("""Enter 1 for enrting the details of the student, 2 for suggesting the diet plan and 3 fr exit""")

choice = int(input("Enter the choice : "))

while choice != 3:
    if choice == 1:
        a = [i for i in input("Enter name, height,weight,sport seperated by commas :").split(",")]
        add_student(a[0],a[1],a[2],a[3])
    elif choice == 2:
        name = input("Enter student name")
        diet_plan(name)
    else:
        print("Enter valid choice")
    choice = int(input("Enter the choice : "))
print("Thanks for using our services")
            
