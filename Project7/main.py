import os
import dt_module
import math_module
import random_module
import uuid_module
import file_module

run = 0
while True:
    run += 1
    if(run == 1):
        print("\n========================")
        print("Welcome to Multi-Utility Toolkit")
        print("========================")
        print("Choose an option:")
    else:
        print("\nChoose an option:")
        print("========================")
    print("1. Date and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")
    print("========================")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            while True:
                dtm = dt_module.DtOperations()
                print("\nDate and Time Operations:")
                print("1. Display current date and time")
                print("2. Calculate difference between two dates/times")
                print("3. Formate date into custom format")
                print("4. Stopwatch")
                print("5. Countdown timer")
                print("6. Back to Main Menu")
                dt_choice = input("Enter your choice: ")
                match dt_choice:
                    case "1":
                        cdt = dtm.current_dt()
                        print(f"\n{cdt}")
                        print("========================")
                    case "2":
                        date1 = input("\nEnter the first date (YYYY-MM-DD): ")
                        date2 = input("Enter the second date (YYYY-MM-DD): ")
                        difference = dtm.difference(date1, date2)
                        print(difference)
                    case "3":
                        format = input("Enter new date format(y,m,d separated by '/'): ")
                        dtm.change_format(format)
                    case "4":
                        time = dtm.stopwatch()
                        print(time)
                        print("========================")
                    case "5":
                        time = int(input("Enter time for timer(in seconds): "))
                        dtm.countdown(time)
                        print("========================")
                    case "6":
                        break
                    case _:
                        print("Invalid option. Please select a valid option from the menu.")
        case "2":
            maths = math_module.MathOperations()
            while True:
                print("\nMathematical Operations:")
                print("1. Calculate Factorial")
                print("2. Solve Compound Interest")
                print("3. Trigonometric Calculations")
                print("4. Area of Geometric Shapes")
                print("5. Back to Main Menu")
                math_choice = input("Enter your choice: ")
                match math_choice:
                    case "1":
                        num = int(input("Enter a number to count factorial: "))
                        factorial = maths.fact(num)
                        print(f"Factorial of {num} is: {factorial}")
                        print("========================")
                    case "2":
                        p = float(input("Enter principal amount: "))
                        r = float(input("Enter rate of interest (in %): "))
                        t = float(input("Enter time (in years): "))
                        ci = maths.compount_interest(p, r, t)
                        print(f"Compound Interest: {ci}")
                        print("========================")
                    case "3":
                        while True:
                            print("\nTrigonometric Calculations")
                            print("1. Sine")
                            print("2. Cosine")
                            print("3. Tan")
                            print("4. Inverse Sine")
                            print("5. Inverse Cosine")
                            print("6. Inverse Tan")
                            print("7. Back to menu")
                            geo_choice = input("Enter what you want to calculate: ")                            
                            match geo_choice:
                                case "1":
                                    angle = float(input("Enter angle(degrees): "))
                                    sine = maths.geo_sin(angle)
                                    print(f"Sine of {angle} is: {sine:.4f}")
                                    print("========================")
                                case "2":
                                    angle = float(input("Enter angle(degrees): "))
                                    cosine = maths.geo_cosine(angle)
                                    print(f"Cosine of {angle} is: {cosine:.4f}")
                                    print("========================")
                                case "3":
                                    angle = float(input("Enter angle(degrees): "))
                                    tan = maths.geo_tan(angle)
                                    print(f"Tan of {angle} is: {tan:.4f}")                                                                        
                                    print("========================")
                                case "4":
                                    angle = float(input("Enter angle(degrees): "))
                                    Isine = maths.geo_Isin(angle)
                                    print(f"Inverse sine of {angle} is: {Isine:.4f}")
                                    print("========================")
                                case "5":
                                    angle = float(input("Enter angle(degrees): "))
                                    Icosine = maths.geo_Icosine(angle)
                                    print(f"Inverse cosine of {angle} is: {Icosine:.4f}")
                                    print("========================")
                                case "6":
                                    angle = float(input("Enter angle(degrees): "))
                                    Itan = maths.geo_Itan(angle)
                                    print(f"Inverse tan of {angle} is: {Itan:.4f}")
                                    print("========================")
                                case "7":
                                    break
                                case _:
                                    print("Invalid option. Please select a valid option from the menu.")
                    case "4":
                        maths.geo_shapes()
                    case "5":
                        break
                    case _:
                        print("Invalid option. Please select a valid option from the menu.")
        case "3":
            rnd = random_module.randomOperations()
            while True:
                print("\nRandom Data Generation:")
                print("1. Generate Random Number")
                print("2. Generate Random List")
                print("3. Create Random Password")
                print("4. Generate Random OTP")
                print("5. Back to Main Menu")
                rand_choice = input("Enter your choice: ")
                match rand_choice:
                    case "1":
                        a = 0
                        start = int(input("Enter starting range: "))
                        end = int(input("Enter ending range: "))
                        if(start > end):
                            a = end
                            end = start
                            start = a
                        randNum = rnd.ran_num(start, end)
                        print(f"\nRandom Number: {randNum}")
                        print("========================")
                    case "2":
                        length = int(input("Enter length of list: "))
                        RandomList = rnd.ran_list(length)
                        print(f"\nRandom list: {RandomList}")
                        print("========================")
                    case "3":
                        length = int(input("\nEnter length of password: "))
                        password = rnd.ran_pass(length)
                        for i,k in enumerate(password):
                            if(i == 0):
                                print("Generated Password: ", end = "")
                            print(k, end = "")
                        print("\n========================")
                    case "4":
                        otp = rnd.ran_otp()
                        for i,k in enumerate(otp):
                            if(i == 0):
                                print("\nGenerated OTP: ", end = "")
                            print(k, end = "")
                        print("\n========================")
                    case "5":
                        break
                    case _:
                        print("Invalid option. Please select a valid option from the menu.")
        case "4":
            ud = uuid_module.UUIDoperation()
            uid = ud.gen_uid()
            print(f"\nGenerated UUID: {uid}")
            print("========================")
        case "5":
            fh = file_module.FileHandling()
            while True:
                print("\nFile Operations:")
                print("1. Create a new file")
                print("2. Write to a file")
                print("3. Read from a file")
                print("4. Append to a file")
                print("5. Delete a file")
                print("6. Back to Main Menu")
                file_choice = input("Enter your choice: ")
                match file_choice:
                    case "1":
                        name = input("Enter file name: ")
                        name = name + ".txt"
                        fh.create_file(name)
                    case "2":
                        name = input("Enter name to write: ")
                        name = name + ".txt"
                        text = input("Enter text to add: ")
                        fh.write_file(name, text)
                    case "3":
                        name = input("Enter file name to read: ")
                        name = name + ".txt"
                        fh.read_file(name)
                    case "4":
                        name = input("Enter file name to append: ")
                        name = name + ".txt"
                        text = input("Enter text to append: ")
                        fh.append_file(name, text)
                    case "5":
                        name = input("Enter file name to delete: ")
                        confirm = input(f"Are you sure you want to delete {name}.txt? (yes/no): ")
                        if(confirm.lower() == "no"):
                            print("File deletion terminated.")
                        elif(confirm.lower() == "yes"):
                            name = name + ".txt"
                            fh.del_file(name)
                        else:
                            print("Invalid option!")
                    case "6":
                        break
                    case _:
                        print("Invalid option. Please select a valid option from the menu.")
        case "6":
            print("\nExplore Module Attributes")
            name = input("Enter module name to explore: ")
            print(f"Available attributes in {name} module:")
            print(dir(name))
        case "7":
            print("\n========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("========================")
            break
        case _:
            print("Invalid option. Please select a valid option from the menu.")