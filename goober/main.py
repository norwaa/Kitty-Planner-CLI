if __name__ == "__main__":
    import csv
    import os
    from tabulate import tabulate

    userinput = ""
    budget_planner = []
    
    
    ## LOADS CSV FILE DATA ##
    def loadBudgetData():
        while True:
            userinput = input("Input CSV Filename. [FORMAT ######]   [.letmeout] - Quit\n") + ".csv"
            magicword = userinput.replace(".", "").lower()
            
            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout (not case sensitive)
                return "Quit"
            
            if os.path.exists(userinput):     ## Checks whether file exists in folder
                print("# Loading CSV Data #".center(65, "_"))
                print("")
                break
            print("")
            print("# File Not Found #".center(65, "_"))
        
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
        
        print(tabulate(data, headers=headers, tablefmt="pipe"))
        print(f"\n\033[4m Monthly Spent. { sum(values) } \033[24m")     ## Using F strings, ANSI escape codes

        while True:
            userinput = input("[R] Return [Q] Quit  ")
            if userinput == "Q" or userinput == "q":
                return "Quit"
            elif userinput == "R" or userinput == "r":
                print("_".center(65, "_"))
                print("")
                break

    ## DISPLAY ADDED RECORDS ##
    def displayRecords(budget_planner):
        for i in range(len(budget_planner)):
            for j in range(len(budget_planner[i])):
                print(budget_planner[i][j], end=" ")
            print("")


    ## ADD NEW RECORDS TO NEW CSV FILE ##
    def addRecords():
        new_table = []
        
        while True:        ## Repeats when values are not confirmed
            userinput = input("Input Values To Be Added. [FORMAT 'TYPE' 'DESCRIPTION' 'ACCOUNT' 'DATE' 'CATAGORY] \n[.letmeout] - Quit\n").split()
            magicword = userinput[0].replace(".", "").lower()
            
            if "letmeout" in magicword and userinput[0][0] == "." and len(userinput) == 1:
                return 
            
            changestate = input("\nConfirm Values? Y/N ")
            if changestate == "Y" or changestate == "y":
                for i in range(0, len(userinput)):
                    new_table.append((userinput[i]))
                budget_planner.append(new_table)
                break        
        return


    ## EXPORT CSV ##
    def exportcsv(budget_planner):
        while True:
            
            userinput = input("Input CSV Filename. [EXISTING FILENAME WILL OVERWRITE] \n[.letmeout] - Quit\n")
            magicword = userinput.replace(".", "").lower()
            
            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                return
            
            changestate = input("\nConfirm Values? Y/N ")
            if changestate == "Y" or changestate == "y":
                name = userinput+".csv"
                with open(name, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(budget_planner)
                print("# File Exported #".center(65,"_"))
                break   


    ## MAIN UI ##
    while True:
        print("")
        print("[ Kikyou Terminal PBP UI ]".center(65, "_"))
        print("_".center(65, "_"))
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
            addRecords()
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
