if __name__ == "__main__":
    import csv
    import os
    
    try:
        from tabulate import tabulate
    except ModuleNotFoundError:
        print("\n!! Tabulate module is not installed. Please install by running 'pip install tabulate' within terminal. !!\n")
        exit()

    try:
        import pandas
    except ModuleNotFoundError:
        print("\n!! Pandas module is not installed. Please install by running 'pip install pandas' within terminal. !!\n")
        exit()
        
    from datetime import datetime
    import pandas as pd
    
    userinput = ""
    budget_planner = []



    ## DISPLAY ADDED RECORDS ##
    def previewEntry(budget_planner):
        headers = ["Type","Description","Account","Date","Category"]
        data = []
        values = []
        for i in range(1, len(budget_planner)):
            data.append(budget_planner[i])
            if budget_planner[i] == "Income":
                values.append(int(budget_planner[i][2]))
            else:
                values.append(-int(budget_planner[i][2]))
        
        print("# Database Preview #".center(66, "_")) 
        print("")
        print(tabulate(data, headers=headers, tablefmt="pipe"))         ## PRINTS TABLE
        while True:
            userinput = input(f"\n\033[4m Monthly Spent. { sum(values) }\033[24m ________________ [Press Enter To Quit.]  ")          ## F STRINGS, ANSI ESCAPE CODES
            return
    
    ## ADD NEW RECORDS TO NEW CSV FILE ##
    def addEntry():
        
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
        
        ## RETURNS SPECIFIC KEYWORD FROM SYNTAX ##  
        def assigndata(userinput, switch):
            while switch == False:
                if userinput.lower() == "i":
                    return "Income"
                if userinput.lower() == "e":
                    return "Expenses"
                return "Invalid"
            while switch != False:
                if userinput.lower() == "u":
                    return "Utilities"
                if userinput.lower() == "t":
                    return "Transport"
                if userinput.lower() == "r":
                    return "Rent"
                if userinput.lower() == "f":
                    return "Food"
                if userinput.lower() == "s":
                    return "Shopping"
                return "Invalid"

        while True:
            new_table = []
            ## ENTER TYPE ##
            while True:
                userinput = input("Enter Entry Type. [I] Income [E] Expenses [.letmeout] Quit\n\n")
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
                    print("")
                    print("# Entries Preview #".center(66, "="))
                    break
                print("\nInvalid Input.")
                print("_".center(66, "_"))

            ## PRINTS PREWVIEW ##    
            print("")
            print(tabulate([new_table], ["Type","Description","Account","Date","Category"], tablefmt="pipe"))
            while True:
                userinput = input("\nConfirm Entries? [Y] Yes [N] No   ")
                if userinput.lower() == "y":
                    budget_planner.append(new_table)
                    while True:
                        userinput = input("Add Another Entry? [Y] Yes [N] No   ")
                        while True:
                            if userinput.lower() == "y":
                                print("_".center(66, "="))
                                return
                            elif userinput.lower() == "n":
                                print("")
                                print("# Database Created #".center(66, "="))
                                return "Quit"
                            break 
                        print("Invalid Input.")
                        print("_".center(66, "_"))
                elif userinput.lower() == "n":
                    print("_".center(66, "_"))
                    return
                print("Invalid Input.")
                print("_".center(66, "_"))
        return "Quit"



    ## EXPORT CSV ##
    def exportcsv(budget_planner):
        while True:
            
            userinput = input("Input Filename. \n[.letmeout] Quit\n\n") + ".csv"
            magicword = userinput.replace(".", "").lower()
            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                return
            print("")
            
            while True:
                changestate = input("Confirm Filename? [Y] Yes [N] No   ")
                if changestate == "Y" or changestate == "y":
                    if os.path.exists(userinput):       ## CHECK WHETHER FILE EXISTS
                        while True:
                            changestate = input("Filename Exists. [O] Overwrite [P] Push   ")
                            if changestate ==  "O" or changestate == "o":
                                with open(userinput, "w", newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(budget_planner)
                                break
                            if changestate == "P" or changestate == "p":
                                with open(userinput, "a", newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(budget_planner)
                                break
                    print("")
                    print("# File Exported #".center(66,"_"))
                    return
                if changestate == "N" or changestate == "n":
                    print("_".center(66, "_"))
                    break

    
    
    ## BROWSING DIRECTORY CSVS ##
    def browseDatabase():
        csvfiles = []
        
         ## LOADS CSV FILE DATA ##
        def loadBudgetData():
            print("=".center(66, "="))
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Loading Mode")
                userinput = input("Input Filename. [FORMAT ######]   [.letmeout] Quit\n\n") + ".csv"
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":         ## LOOKS FOR ".lmetout"
                    return "Quit"
                
                if os.path.exists(userinput):       ## CHECK WHETHER FILE EXISTS
                    print("# Loading CSV Data #".center(66, "_"))
                    print("")
                    break
                print("")
                print("# File Not Found #".center(66, "="))

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
                userinput = input(f"\n\033[4m Monthly Spent. { sum(values) }\033[24m _________________ [R] Return [Q] Quit  ")          ## F STRINGS, ANSI ESCAPE CODES
                if userinput.lower() == "q":
                    return "Quit"
                elif userinput.lower() == "r":
                    print("")
                    break
        
        
        ## DELETE FILE FROM DIRECTORY ##
        def deleteData():
            print("=".center(66, "="))
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Deletion Mode.")
                userinput = input("Input Filename. [.letmeout] Quit\n\n") + ".csv"
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                    return
                print("")
                
                while True:
                    changestate = input("Confirm Filename? [DELETION CANNOT BE REVERTED.]  [Y] Yes [N] No  ")
                    if changestate == "Y" or changestate == "y":
                        if os.path.exists(userinput):       ## CHECK WHETHER FILE EXISTS
                            print("")
                            for i in range(0, len(csvfiles)):
                                if userinput in csvfiles[i]:
                                    csvfiles.pop(i)
                            os.remove(userinput)
                            print("# Database Removed #".center(66, "="))
                        else:
                            print("")
                            print("# File Does Not Exist #".center(66, "="))
                            break
                    if changestate == "N" or changestate == "n":
                        print("_".center(66, "_"))
                    break
            return    
        
        ## MAIN BROWSE MODE UI ##
        counter = 0        
        for files in os.listdir(os.path.dirname(__file__)):         ## LIST ALL CSV EXTENSION FILES
            if files.endswith(".csv"):
                counter += 1
                csvfiles.append([files])
        if counter == 0:
            print("No Databases Are Found.")
            return 
        
        while True:
            print("")
            print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
            print("\nCurrently - Overview Mode.")
            userinput = input("[L] Load Database [D] Delete Database [.letmeout] Quit   ")
            magicword = userinput.replace(".", "").lower()
            if userinput.lower() == "l":
                while True:
                    if loadBudgetData() == "Quit":
                        break
                print("")
                print("=".center(66, "="))
            if userinput.lower() == "d":
                deleteData()
                print("=".center(66, "="))
            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                return
        return

                
    ## MAIN UI ##
    while True:
        print("")
        print("[ Kikyou TUI Budget Planner ]".center(66, "="))
        print("_".center(66, "_"))
        print("")
        print("[1] Browse Database Library")
        print("[2] Preview Recent Database")
        print("[3] Create Database")
        print("[4] Export Database As CSV")
        print("[Q] Quit")
        print("_".center(66, "_"))
        userinput = input("Waiting for input..  ")
        print("")

        if userinput == "1":
            print("=".center(66, "="))
            browseDatabase()
        elif userinput == "2":
            print("=".center(66, "="))    
            print("")
            previewEntry(budget_planner)
            print("")
            pass
        elif userinput == "3":
            print("=".center(66, "="))
            print("") 
            while True:
                if addEntry() == "Quit":
                    break
            pass
        elif userinput == "4":
            print("=".center(66, "="))    
            print("")
            exportcsv(budget_planner)
            print("")
            pass
        elif userinput.lower() == "q":
            print("=".center(66, "="))
            print("\nQuit.\n")
            exit()
