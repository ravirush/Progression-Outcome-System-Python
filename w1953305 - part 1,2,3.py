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
#code
while True:
    p_count = 0                                                                #defining variables for count and list
    t_count = 0
    r_count = 0
    e_count = 0
    progress_list = []
    trailer_list = []
    retriever_list = []
    exclude_list = []
    student_staff = input("Enter   1-for student\n\t2-for admin\nEnter here: ")#checking whether the program is run by a student or a staff member
    print()                                                                    
    if student_staff == "1":                                                   #starting the student program
        while True:
            Pass = check_score_student("Pass")                                 #calling user defined function
            Defer = check_score_student("Differ")
            Fail = check_score_student("Fail")

            total = Pass + Defer + Fail                                        #checking total
            if total != 120:
                print("Total incorrect\n")
                continue
            else:
                if Pass == 120:                                                #checking appropriate progression outcomes and display it
                    print("Progress")               
                elif Pass == 100:
                    print("Progress (module trailer)")        
                elif Fail >= 80:
                    print("Exclude")   
                else:
                    print("Module retriever")
                print()
                break
            
    elif student_staff == "2":                                                 #starting the student program
        while True:
            Pass = check_score_staff("Pass")                                   #calling user defined function
            Defer = check_score_staff("Differ")
            Fail = check_score_staff("Fail")

            total = Pass + Defer + Fail                                        #checking total
            if total != 120:
                print("Total incorrect\n")
                continue
            else:
                if Pass == 120:                                                #checking appropriate progression outcomes, displaying it and counting it
                    print("Progress")
                    p_count += 1
                    progress_list.append((Pass,Defer,Fail))                    #appending credit values for the list
                elif Pass == 100:
                    print("Progress (module trailer)")
                    t_count += 1
                    trailer_list.append((Pass,Defer,Fail))
                elif Fail >= 80:
                    print("Exclude")
                    e_count += 1
                    exclude_list.append((Pass,Defer,Fail))
                else:
                    print("Module retriever")
                    r_count += 1
                    retriever_list.append((Pass,Defer,Fail))
                print()
          
            while True:
                #asking from staff member 'y' to enter another set of student data and 'q' to quit and view results
                choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower() 
                if choice == "y":
                    print()
                    break
                elif choice == "q":                                                    #printing histogram
                    print()
                    print("-"*64)
                    print("Histogram")
                    print("Progress ", p_count, ":", p_count * '*')
                    print("Trailer  ", t_count, ":", t_count * '*')
                    print("Retriever", r_count, ":", r_count * '*')
                    print("Excluded ", e_count, ":", e_count * '*')
                    print()
                    print(p_count+t_count+r_count+e_count, "outcomes in total.")
                    print("-"*64)

                    print("part 2:")                                                   #listed data reading and printing 
                    for a in range(p_count):
                        #I used (*value,sep=",") to print a list without brackets and seperate each element with a comma followed by a space, reference from :- https://www.studytonight.com/post/the-sep-and-end-parameters-in-python-print-statement
                        print("Progress -", *progress_list[a],sep=", ")                 
                    for b in range(t_count):
                        print("Progress (module trailer) -", *trailer_list[b],sep=", ")
                    for c in range(r_count):
                        print("Module retriever -", *retriever_list[c],sep=", ")
                    for d in range(e_count):
                        print("Exclude -", *exclude_list[d],sep=", ")

                    print()
                    file = open("outcomes.txt", "w")                                                      #saving listed data to a text file and and printing
                    file.write("Part 3:\n")
                    for a in range(p_count):
                        file.write("Progress - "+ str(progress_list[a]).strip('()') +"\n")   
                    for b in range(t_count):
                        file.write("Progress (module trailer) - "+ str(trailer_list[b]).strip('()') +"\n")
                    for c in range(r_count):
                        file.write("Module retriever - "+ str(retriever_list[c]).strip('()') +"\n")
                    for d in range(e_count):
                        file.write("Exclude - "+ str(exclude_list[d]).strip('()') +"\n")
                    file.close()
                    file = open("outcomes.txt", "r")
                    print(file.read())
                    file.close
                    raise SystemExit                            #raise SystemExit used for exit the program, reference from :- https://adamj.eu/tech/2021/10/10/the-many-ways-to-exit-in-python/
                else:
                    print("Enter valid input\n")            
    else:
        print("Enter valid input")
        
