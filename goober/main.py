if __name__ == "__main__":
    import csv
    import os
    from tabulate import tabulate
    from datetime import datetime

    userinput = ""
    budget_planner = [["Type","Description","Account","Date","Category"]]



    ## LOADS CSV FILE DATA ##
    def loadBudgetData():
        while True:
            userinput = input("Input CSV Filename. [FORMAT ######]   [.letmeout] - Quit\n\n") + ".csv"
            magicword = userinput.replace(".", "").lower()

            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout (not case sensitive)
                return "Quit"

            if os.path.exists(userinput):     ## Checks whether file exists in folder
                print("# Loading CSV Data #".center(66, "_"))
                print("")
                break
            print("")
            print("# File Not Found #".center(66, "_"))

        filename = str(userinput)
        data = []
        values = []
        with open(filename, "r") as file:
            obtainedheader = False
            reader = csv.reader(file)
            list_of_rows = list(reader)

            for i in range(len(list_of_rows)):
                if obtainedheader != True:
                    headers = list_of_rows[i]
                    obtainedheader = True
                else:
                    data.append(list_of_rows[i])
                    if list_of_rows[i][0] == "Income":
                        values.append(int(list_of_rows[i][2]))
                    else:
                        values.append(-int(list_of_rows[i][2]))

        ## PRINTS TABLE ##
        print(tabulate(data, headers=headers, tablefmt="pipe"))
        while True:
            userinput = input(f"\n\033[4m Monthly Spent. { sum(values) }\033[24m _________________ [R] Return [Q] Quit  ")          ## Using F strings, ANSI escape codes
            if userinput == "Q" or userinput == "q":
                return "Quit"
            elif userinput == "R" or userinput == "r":
                print("_".center(66, "_"))
                break



    ## DISPLAY ADDED RECORDS ##
    def displayRecords(budget_planner):
        headers = budget_planner[0]
        data = []
        values = []
        for i in range(1, len(budget_planner)):
            data.append(budget_planner[i])
            if budget_planner[i] == "Income":
                values.append(int(budget_planner[i][2]))
            else:
                values.append(-int(budget_planner[i][2]))
                
        ## PRINTS TABLE ##
        print(tabulate(data, headers=headers, tablefmt="pipe"))
        while True:
            userinput = input(f"\n\033[4m Monthly Spent. { sum(values) }\033[24m ________________ [Press Enter To Quit.]  ")          ## Using F strings, ANSI escape codes
            return
    
    ## ADD NEW RECORDS TO NEW CSV FILE ##
    def addRecords():
        
        ## LOOKS FOR THE KEYWORD "".LETMEOUT" ON EVERY INPUT ##
        def letmeout(userinput):
            magicword = userinput.replace(".", "").lower()
            if "letmeout" in magicword and userinput[0] == ".":
                return True
        
        ## VALIDATES DATA ##
        def validate(userinput):
            try:
                datetime.strptime(userinput, "%m.%d.%Y")
                return True
            except ValueError:
                return False
            
        def assigndata(userinput, switch):
            while switch == False:
                if userinput == "I" or userinput == "i":
                    return "Income"
                if userinput == "E" or userinput == "e":
                    return "Expenses"
                return "Invalid"
                
            while switch != False:
                if userinput == "U" or userinput == "u":
                    return "Utilities"
                if userinput == "T" or userinput == "t":
                    return "Transport"
                if userinput == "R" or userinput == "r":
                    return "Rent"
                if userinput == "F" or userinput == "f":
                    return "Food"
                if userinput == "S" or userinput == "s":
                    return "Shopping"
                return "Invalid"


        while True:
            new_table = []
            ## ENTER TYPE ##
            while True:
                userinput = input("Enter Data Type. [I] Income [E] Expenses [.letmeout] Quit\n\n")
                if letmeout(userinput) == True:
                    return("Quit")
                if assigndata(userinput, False) != "Invalid":
                    new_table.append(assigndata(userinput, False))
                    print("_".center(66, "_"))
                    break
                print("\nInvalid Input.")
                print("_".center(66, "_"))
            
            
            ## ENTER DESCRIPTION ##
            userinput = input("Enter Description. [Enter To Leave Blank] [.letmeout] Quit\n\n")
            if letmeout(userinput) == True:
                return("Quit")
            print("_".center(66, "_"))
            new_table.append(userinput)
            
            
            ## ENTER ACCOUNT ##
            while True:   
                userinput = input("Enter Account. [.letmeout] Quit\n\n")
                if letmeout(userinput) == True:
                    return("Quit")
                try:
                    new_table.append((int(userinput)))
                    print("_".center(66, "_"))
                    break
                except ValueError:
                    print("\nInvalid Input.")
                    print("_".center(66, "_"))
               
               
            ## ENTER DATE ##
            while True: 
                userinput = input("Enter Date. [FORMAT MM.DD.YYYY] [.letmeout] Quit\n\n")
                if letmeout(userinput) == True:
                    return("Quit")
                
                if validate(userinput) == True:
                    print("_".center(66, "_"))
                    new_table.append(userinput)
                    break
                print("\nInvalid Date.")
                print("_".center(66, "_"))
            
            
            ## ENTER CATAGORY ##
            while True:
                userinput = input("Enter Catagory. [.letmeout] Quit \n[U] Utilities [T] Transport [R] Rent [F] Food [S] Shopping\n\n")
                if letmeout(userinput) == True:
                    return("Quit")
                if assigndata(userinput, True) != "Invalid":
                    new_table.append(assigndata(userinput,True))
                    print("_".center(66, "_"))
                    break
                print("\nInvalid Input.")
                print("_".center(66, "_"))
            
            
            ## PRINTS PREWVIEW ##    
            print("Record Preview.")
            print(tabulate([new_table], ["Type","Description","Account","Date","Category"], tablefmt="pipe"))
            while True:
                userinput = input("\nConfirm Values? [Y] Yes [N] No      ")
                if userinput == "Y" or userinput == "y":
                    budget_planner.append(new_table)
                    while True:
                        userinput = input("Add Another Record? [Y] Yes [N] No   ")
                        while True:
                            if userinput == "Y" or userinput == "y":
                                print("_".center(66, "_"))
                                return
                            elif userinput == "N" or userinput == "n":
                                return "Quit"
                                print("_".center(66, "_"))
                            break 
                        print("Invalid Input.")
                        print("_".center(66, "_"))
                elif userinput == "N" or userinput == "n":
                    print("_".center(66, "_"))
                    return
                print("Invalid Input.")
                print("_".center(66, "_"))
        return "Quit"



    ## EXPORT CSV ##
    def exportcsv(budget_planner):
        while True:

            userinput = input("Input CSV Filename. [EXISTING FILENAME WILL OVERWRITE] \n[.letmeout] - Quit\n")
            magicword = userinput.replace(".", "").lower()

            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                return

            changestate = input("\nConfirm Filename? Y/N ")
            if changestate == "Y" or changestate == "y":
                name = userinput+".csv"
                with open(name, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(budget_planner)
                print("# File Exported #".center(66,"_"))
                break   



    ## MAIN UI ##
    while True:
        print("")
        print("[ Kikyou Terminal PBP UI ]".center(66, "_"))
        print("_".center(66, "_"))
        print("[1] Load CSV Data")
        print("[2] Display Recent Records")
        print("[3] Add New Records")
        print("[4] Export Records")
        print("[Q] Quit")
        print("_".center(65, "_"))
        userinput = input("Waiting for input..   ")

        if userinput == "1":
            print("_".center(65, "_"))    
            while True:
                if loadBudgetData() == "Quit":
                    break
            print("")
        elif userinput == "2":
            print("_".center(65, "_"))
            displayRecords(budget_planner)
            print("")
            pass
        elif userinput == "3":
            print("_".center(65, "_"))
            while True:
                if addRecords() == "Quit":
                    break
            print("")
            pass
        elif userinput == "4":
            print("_".center(65, "_"))
            exportcsv(budget_planner)
            print("")
            pass
        elif userinput == "Q" or userinput == "q":
            print("Quit.")
            break
