if __name__ == "__main__":
    import csv
    import os
    
    userinput = ""
    budget_planner = []

    def loadBudgetData():       ## Loads csv file data
        
        while True:
            csvname = input("Input CSV Filename. [FORMAT ######]   [.letmeout] - Quit\n") + ".csv"

            if ".letmeout" in csvname:      ## Triggers when csvname contains .letmeout
                print("")
                print("\nQuit.")
                return
            
            if os.path.exists(csvname):     ## Checks whether file exists in folder
                print("# Loading CSV Data #".center(60,"_"))
                print("")
                break
            print("")
            print("# File Not Found #".center(60,"_"))
        
        filename = str(csvname)
        two_d_list = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            list_of_rows = list(reader)
            for i in range(len(list_of_rows)):
                two_d_list.append(list_of_rows[i])
                
        for i in two_d_list:
            print(i)
        
        return 

    def displayRecords(budget_planner):
        for i in range(len(budget_planner)):
            for j in range(len(budget_planner[i])):
                print(budget_planner[i][j], end=" ")
            print("")

    def addRecords():       ## Adds new records to the new csv file
        new_table = []
        
        while True:        ## Repeats when values are not confirmed
            userinput = input("Input Values To Be Added. [FORMAT ### ### ###...] \n[.letmeout] - Quit\n").split()
            
            if ".letmeout" in userinput:      ## Triggers when csvname contains .letmeout
                print("\nQuit.")
                return        
            
            changestate = input("\nConfirm Values? Y/N ")
            if changestate == "Y" or changestate == "y":
                for i in range(0, len(userinput)):
                    new_table.append((userinput[i]))
                budget_planner.append(new_table)
                break        
        return
        
    def exportcsv(budget_planner):
        while True:
            
            userinput = input("Input CSV Filename. [EXISTING FILENAME WILL BE OVERWRITED] \n[.letmeout] - Quit\n")
            if ".letmeout" in userinput:      ## Triggers when csvname contains .letmeout
                print("")
                print("Quit.")
                return
            
            changestate = input("\nConfirm Values? Y/N ")
            if changestate == "Y" or changestate == "y":
                name = userinput+".csv"
                with open(name, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(budget_planner)
                print("# File Exported #".center(60,"_"))
                break   

    while True:
        print("")
        print("[ Kikyou Terminal PBP UI ]".center(60,"_"))
        print("_".center(60,"_"))
        print("[1] Load CSV Data")
        print("[2] Display Recent Records")
        print("[3] Add New Records")
        print("[4] Export Records")
        print("[Q] Quit")
        print("_".center(60,"_"))
        userinput = input("Waiting for input..   ")

        if userinput == "1":
            print("_".center(60,"_"))
            print("triggered 1")
            loadBudgetData()
            print("")
            pass
        elif userinput == "2":
            print("_".center(60,"_"))
            displayRecords(budget_planner)
            print("")
            pass
        elif userinput == "3":
            print("_".center(60,"_"))
            addRecords()
            print("")
            pass
        elif userinput == "4":
            print("_".center(60,"_"))
            exportcsv(budget_planner)
            print("")
            pass
        elif userinput == "Q" or userinput == "q":
            print("Quit.")
            break
