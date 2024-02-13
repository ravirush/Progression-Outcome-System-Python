# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953305
# Date: 12/14/2022

#ask user for inputs and check inputs in range or not : this user defined function is for students
def check_score_student(score):
    while True:
        try:
            credit = int(input(f"Please enter your credits at {score}: "))
            if credit not in range(0, 121, 20):
                print("Out of range\n")
            else:
                return credit
        except ValueError:
            print("Integer required\n")

#ask user for inputs and check inputs in range or not : this user defined function is for staff members
def check_score_staff(score):
    while True:
        try:
            credit = int(input(f"Enter your total {score} credits: "))
            if credit not in range(0, 121, 20):
                print("Out of range\n")
            else:
                return credit
        except ValueError:
            print("Integer required\n")
            
#ask user for student id input and checking it
def ID():
    while True:
        student_id = input("Enter your Student ID: ").lower()
        if student_id[0]=='w':
            if len(student_id)==8:
                for num in student_id[1:]:
                    if num.isdigit():
                        return student_id
                    else:
                        print('Invalid ID')
            else:
                print('Invalid ID')
        else:
            print('Invalid ID')

#code
while True:
    outcomes_dictionary = {}                                                    #defining a variables for dictionary
    student_staff = input("Enter   1-for student\n\t2-for admin\nEnter here: ") #checking whether the program is run by a student or a staff member
    print()
    if student_staff == "1":                                                    #starting the student program
        while True:
            student_id = ID()                                                   #calling user defined function
            Pass = check_score_student("Pass")
            Defer = check_score_student("Differ")
            Fail = check_score_student("Fail")

            total = Pass + Defer + Fail                                         #checking total
            if total != 120:
                print("Total incorrect\n")
                continue
            else:
                if Pass == 120:                                                 #checking appropriate progression outcomes and display it with student id
                    print(f"{student_id} : Progress")               
                elif Pass == 100:
                    print(f"{student_id} : Progress (module trailer)")        
                elif Fail >= 80:
                    print(f"{student_id} : Exclude")   
                else:
                    print(f"{student_id} : Module retriever")
                print()
                break
            
    elif student_staff == "2":                                                  #starting the staff program
        while True:
            student_id = ID()                                                   #calling user defined function
            Pass = check_score_staff("Pass")
            Defer = check_score_staff("Differ")
            Fail = check_score_staff("Fail")

            total = Pass + Defer + Fail                                         #checking total
            if total != 120:
                print("Total incorrect\n")
                continue
            else:
                if Pass == 120:                                                         #checking appropriate progression outcomes, displaying it 
                    print(f"{student_id} : Progress")
                    data_set = (f"Progress - {Pass}, {Defer}, {Fail}")
                    outcomes_dictionary[student_id] = data_set                          #creating a dictionary
                elif Pass == 100: 
                    print(f"{student_id} : Progress (module trailer)")
                    data_set = (f"Progress (module trailer) - {str(Pass)}, {str(Defer)}, {str(Fail)}")
                    outcomes_dictionary[student_id] = data_set
                elif Fail >= 80:
                    print(f"{student_id} : Exclude")
                    data_set = (f"Exclude - {str(Pass)}, {str(Defer)}, {str(Fail)}")
                    outcomes_dictionary[student_id] = data_set
                else:
                    print(f"{student_id} : Module retriever")
                    data_set = (f"Module retriever - {str(Pass)}, {str(Defer)}, {str(Fail)}")
                    outcomes_dictionary[student_id] = data_set
                print()
          
            while True:
                #asking from staff member 'y' to enter another set of student data and 'q' to quit and view results
                choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
                if choice == "y":
                    print()
                    break
                elif choice == "q":
                    print()
                    print("Part 4:")                     #displaying created dictionary
                    for key in outcomes_dictionary:
                        print(f"{key} : {outcomes_dictionary[key]}", end=" ")
                    raise SystemExit                     #raise SystemExit used for exit the program, reference from :- https://adamj.eu/tech/2021/10/10/the-many-ways-to-exit-in-python/
                else:
                    print("Enter valid input\n")            
    else:
        print("Enter valid input")
        

