if __name__ == "__main__":
    import csv
    import os
    from datetime import datetime

    try:
        from tabulate import tabulate
    except ModuleNotFoundError:
        print("\n!! Tabulate module is not installed. Please install by running 'pip install tabulate' within terminal. !!\n")
        exit()

    try:
        import pandas as pd
    except ModuleNotFoundError:
        print("\n!! Pandas module is not installed. Please install by running 'pip install pandas' within terminal. !!\n")
        exit()

    try:
        import pyfiglet
    except ModuleNotFoundError:
        print("\n!! Pyfiglet module is not installed. Please install by running 'pip install pyfiglet' within terminal. !!\n")
        exit()

    print("")
    print("")
    print(pyfiglet.figlet_format("ARKY", font="alligator", justify="center", width=66))         ## STARTUP ASCII ART

    #userinput = ""
    budget_planner = [["Type","Description","Account","Date","Category"]]

    if os.getcwd() != os.path.dirname(__file__):
        os.chdir(os.getcwd()+"/goober")


    ## INPUT DATE ##
    def inputDate():
        while True:
            userinput = input("Enter Date. [FORMAT YYYY.MM.DD [1678 - 2261]] [.letmeout] Quit\n\n")
            if letmeout(userinput) == True:
                return "Quit"

            if validate(userinput) == True:
                print("_".center(66, "_"))
                new_table.append(userinput)
                break
            print("\nInvalid Date.")
            print("_".center(66, "_"))
        return
    
    
    ## INPUT CATAGORY ##
    def inputCatagory():
        pass
        

    ## DISPLAY ADDED RECORDS ##
    def previewEntry(budget_planner):
        headers = budget_planner[0]
        data = []
        values = []
        for i in range(1, len(budget_planner)):
            data.append(budget_planner[i])
            print(budget_planner[i][0])

            values.append(int(budget_planner[i][2]))

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
                if len(userinput) == 10:
                    date = datetime.strptime(userinput, "%Y.%m.%d")
                    if 1677 < date.year < 2262:
                        return True
                return False
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
                    if userinput.isdigit() == True:
                        if new_table[0] == "Income":
                            new_table.append((int(userinput)))
                        else:
                            new_table.append(-int(userinput))
                        print("_".center(66, "_"))
                        break
                except ValueError:
                    pass

                print("\nInvalid Input.")
                print("_".center(66, "_"))

            ## ENTER DATE ##
            while True:
                userinput = input("Enter Date. [FORMAT YYYY.MM.DD [1678 - 2261]] [.letmeout] Quit\n\n")
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
                    print("")
                    print("# Entries Preview #".center(66, "="))
                    break
                print("\nInvalid Input.")
                print("_".center(66, "_"))

            ## PRINTS PREVIEW ##
            print("")
            print(tabulate([new_table], ["Type","Description","Account","Date","Category"], tablefmt="pipe"))
            while True:
                userinput = input("\nConfirm Entries? [Y] Yes [N] No   ")
                if userinput.lower() == "y":
                    budget_planner.append(new_table)
                    while True:
                        userinput = input("Add Another Entry? [Y] Yes [N] No   ")
                        print("")
                        while True:
                            if userinput.lower() == "y":
                                print("=".center(66, "="))
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
                                with open(userinput, "w", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(budget_planner)

                            if changestate == "P" or changestate == "p":
                                with open(userinput, "a", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(budget_planner)

                    else:
                        with open(userinput, "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(budget_planner)
                        print("")
                        print("# File Exported #".center(66,"_"))
                    return
                if changestate == "N" or changestate == "n":
                    print("_".center(66, "_"))
                    break



    ## BROWSING DIRECTORY CSVS ##
    def browseDatabase():
        csvfiles = []

         ## LOADING MODE ##
        def loadBudgetData():
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Loading Mode")
                print("")
                userinput = str(input("Input Filename. [FORMAT ######]  [.letmeout] Quit\n")) + ".csv"
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":         ## LOOKS FOR ".lmetout"
                    return "Quit"

                try:
                    int(userinput)
                except ValueError:
                    str(userinput)

                data = []
                values = []

                if os.path.exists(userinput):       ## CHECKS WHETHER FILE EXISTS && GRABS ALL DATA FROM DATABASE
                    with open(userinput, "r") as file:
                        obtainedheader = False
                        reader = csv.reader(file)
                        list_of_rows = list(reader)

                        for i in range(len(list_of_rows)):
                            if obtainedheader != True:
                                headers = list_of_rows[i]
                                obtainedheader = True
                            else:
                                data.append(list_of_rows[i])
                                values.append(int(list_of_rows[i][2]))

                    if len(data) == 0:
                        print("# Empty Database #".center(66, "="))
                    else:
                        print("")
                        print("# Loading CSV Data #".center(66, "_"))
                        print("")
                        print(tabulate(data, headers=headers, tablefmt="pipe"))         ## PRINTS TABLE
                        while True:
                            userinput = input(f"\n\033[4m Monthly Spent. { sum(values) }\033[24m _________________ [R] Return [Q] Quit  ")          ## F STRINGS, ANSI ESCAPE CODES
                            if userinput.lower() == "q":
                                return "Quit"
                            elif userinput.lower() == "r":
                                print("")
                                break
                            break
                else:
                    print("")
                    print("# File Not Found #".center(66, "="))


        ## DELETION MODE ##
        def deleteData():
            print("=".center(66, "="))
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Deletion Mode.")
                print("")
                userinput = str(input("Input Filename. [FORMAT ######] [.letmeout] Quit\n")) + ".csv"
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                    return
                print("")

                while True:
                    changestate = input("Confirm Filename? [DELETION CANNOT BE REVERTED.] [Y] Yes [N] No  ")
                    if changestate == "Y" or changestate == "y":
                        if os.path.exists(userinput):       ## CHECK WHETHER FILE EXISTS
                            print("")
                            for item in csvfiles:
                                for name in item:
                                    if name == userinput:
                                        csvfiles.remove(item)

                            os.remove(userinput)
                            print("# Database Removed #".center(66, "="))
                            break
                        else:
                            print("")
                            print("# File Not Found #".center(66, "="))
                            break
                    if changestate == "N" or changestate == "n":
                        print("_".center(66, "_"))
                        break



        ## SEARCH MODE ##
        def searchData():
            ## .letmeout ##
            def letmeout(userinput):
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":
                    return True


            ## SORT DATABASE ##
            def sortDatabase(data, values):
                print("_".center(66, "_"))
                headers=["Type","Description","Account","Date","Category"]
                sortingdate = False
                mode = ""
                df = pd.DataFrame(data, columns=headers)

                ## BY ACCOUNT OR DATE OR CATEGORY ##
                def sortby():
                    nonlocal mode
                    nonlocal sortingdate
                    while True:
                        userinput = input("Sort By? [T] Type [A] Account [D] Date [C] Category   ")
                        if userinput.lower() == "a":
                            mode = "Account"
                            return mode
                        elif userinput.lower() == "d":
                            #nonlocal sortingdate
                            sortingdate = True
                            df["Date"] = pd.to_datetime(df["Date"], format='%Y.%m.%d')
                            mode = "Date"
                            return mode
                        elif userinput.lower() == "c":
                            mode = "Category"
                            return mode
                        elif userinput.lower() == "t":
                            mode = "Type"
                            return mode
                        print("")
                        print("Invalid Input.")

                ## ASCENDING OR DESCENDING ##
                def asc_des():
                    global order
                    while True:
                            userinput = input("Ascending/Descending? [A][D]   ")
                            if userinput.lower() == "a":
                                order = "Ascending"
                                return True
                            if userinput.lower() == "d":
                                order = "Descending"
                                return False
                            print("")
                            print("Invalid Input.")

                sorted_df = df.sort_values(by=sortby(), ascending=asc_des())
                if sortingdate == True:
                    sorted_df["Date"] = sorted_df["Date"].dt.strftime('%Y.%m.%d')

                values = []
                for i in range(0, len(data)):
                    values.append(int(data[i][2]))

                print("")
                print(f"# Sorted Records By {mode} ({order}) Within Directory #".center(66, "="))
                print("")
                print(tabulate(sorted_df, headers=["Type","Description","Account","Date","Category"], tablefmt="pipe", showindex=False))
                userinput = input(f"\n\033[4m Total Spent. { sum(values) }\033[24m ___________________ [Press Enter To Quit.]  ")          ## F STRINGS, ANSI ESCAPE CODES
                return


            ## GLOBAL SEARCH ##
            def globalSearch():
                while True:
                    print("_".center(66, "_"))
                    userinput = input("Input Keyword/Value. [D] Disable Global Search [S] Sort Directory \n")
                    print("")
                    if userinput.lower() == "d":
                        print("=".center(66, "="))
                        return

                    try:
                        int(userinput)
                    except ValueError:
                        str(userinput)

                    filenames = []
                    headers = ["Type","Description","Account","Date","Category"]
                    data = []
                    values = []
                    matchedrecord = []
                    matchedvalues = []

                    for files in os.listdir(os.path.dirname(__file__)):         ## LIST ALL CSV EXTENSION FILES
                        if files.endswith(".csv"):
                            filenames.append(files)

                    for stuff in filenames:
                        with open(stuff, "r") as file:
                            reader = csv.reader(file)
                            list_of_rows = list(reader)
                            for i in range(1, len(list_of_rows)):
                                    data.append(list_of_rows[i])
                                    values.append(int(list_of_rows[i][2]))

                        for record in list_of_rows:
                            for item in record:
                                if item == userinput:
                                    matchedrecord.append(record)
                                    matchedvalues.append(int(record[2]))

                    if userinput.lower() == "s":
                        sortDatabase(data, values)
                        print("")
                        print("=".center(66, "="))
                    else:
                        if len(matchedrecord) == 0:
                            print("No Matching Results.")
                            print("_".center(66, "_"))
                        else:
                            print("")
                            print("# Search Result Within All Databases #".center(66, "="))
                            print("")
                            print(tabulate(matchedrecord, headers=headers, tablefmt="pipe"))
                            userinput = input(f"\n\033[4m Total Spent. { sum(matchedvalues) }\033[24m ___________________ [Press Enter To Quit.]  ")
                            print("")


            ## MAIN FILE SEARCH ##
            print("=".center(66, "="))
            while True:
                while True:     ## CHECKS WHETHER FILE EXISTS
                    print("")
                    print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                    print("\nCurrently - Search Mode.")
                    print("")

                    userinput = str(input("Input Filename. [FORMAT ######] [G] Global Search [.letmeout] Quit\n"))
                    if letmeout(userinput) == True:
                        return
                    print("")

                    if userinput.lower() == "g":
                        globalSearch()
                        break
                    else:
                        if os.path.exists(userinput+".csv"):
                            filename = userinput+".csv"
                            headers=["Type","Description","Account","Date","Category"]
                            data = []

                           # while letmeout(userinput) != True:  ## GRABS ALL DATA FROM DATABASE
                            with open(userinput+".csv", "r") as file:
                                reader = csv.reader(file)
                                list_of_rows = list(reader)

                            try:
                                for i in range(1, len(list_of_rows)):
                                    data.append(list_of_rows[i])
                            except IndexError:
                               pass

                            if len(data) == 0:
                                print("# Empty Database #".center(66, "="))
                                break

                            ## LOOPS THROUGH EVERY ITEM WITHIN RECORDS IN DATABASE AND FINDS MATCHING KEYWORD/VALUE ##
                            while True:
                                print("_".center(66, "_"))
                                userinput = input(f"Input Keyword/Value. [Currently In {filename}] [.letmeout] Quit\n")
                                print("")
                                if letmeout(userinput) == True:
                                    print("=".center(66, "="))
                                    break
                                try:
                                    int(userinput)
                                except ValueError:
                                    str(userinput)

                                matchedrecord = []
                                matchdvalues = []

                                for record in data:
                                    for item in record:
                                        if item == userinput:
                                            record[2] = int(record[2])
                                            matchedrecord.append(record)
                                            matchdvalues.append(int(record[2]))

                                print(matchedrecord)

                                if len(matchedrecord) == 0:
                                    print("No Matching Results.")
                                    print("_".center(66, "_"))
                                else:
                                    print("# Search Results #".center(66, "="))
                                    print("")
                                    print(tabulate(matchedrecord, headers=headers, tablefmt="pipe"))
                                    userinput = input(f"\n\033[4m Total Spent. { sum(matchdvalues) }\033[24m __________ [S] Sort [Press Enter To Quit.]  ")

                                    if userinput.lower() == "s":
                                        sortDatabase(matchedrecord, matchdvalues)
                                    print("")
                        else:
                            print("")
                            print("# File Not Found #".center(66, "="))


        ## EDIT DATABASE ##
        def editDatabase():

            ## EDIT ROW ##
            def editrow(row, columnindex, action):
                print(row[columnindex])

                def swapItem(userinput):
                    if userinput == "i":
                        return "Income"
                    if userinput == "e":
                        return "Expenses"
                    
                    if userinput == "u":
                        return "Utilities"
                    if userinput == "t":
                        return "Transport" 
                    if userinput == "r":
                        return "Rent"
                    if userinput == "f": 
                        return "Food"
                    if userinput == "s":
                        return "Shopping"
                     
                    
                    
                    
                    
                    return "Invalid" 
                pass

                if row[columnindex] in ["Income", "Expenses"]:
                    print("it is indeed income or expenses")
                    if action == "d":
                        dummydata.pop(rowindex)
                        print(dummydata)

                    if action == "e":
                        print("Editing Income/Expenses")
                        while True:
                            userinput = input("Input New Value. [I] Income [E] Expenses   ").lower()       
                            if swapItem(userinput) != "Invalid":
                                row[columnindex] = swapItem(userinput)
                                print("")
                                print(tabulate([row], tablefmt="github"))
                                break
                            else:
                                print("Invalid Input")
                        pass

                print("")
                print("EDIT ROW FUNCTION ENDED")
                pass

            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Edit Mode.")
                print("")
                userinput = str(input("Input Filename. [FORMAT ######] [.letmeout] Quit\n")) + ".csv"
                magicword = userinput.replace(".", "").lower()
                if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                    return
                print("")

                if os.path.exists(userinput):
                    filename = userinput
                    dummydata = []
                    headers = ["Type","Description","Account","Date","Category"]
                    #values = []
                    with open(userinput, "r") as file:
                        reader = csv.reader(file)
                        list_of_rows = list(reader)
                        for i in range(1, len(list_of_rows)):
                            dummydata.append(list_of_rows[i])
                            #values.append(int(list_of_rows[i][2]))

                    if len(dummydata) == 0:
                        print("# Empty Database #".center(66, "="))
                    else:
                        print("")
                        print("# Loading CSV Data #".center(66, "_"))
                        print("")
                        print(tabulate(dummydata, headers=headers, tablefmt="pipe", showindex=True))
                        while True:
                            try:
                                rowindex = int(input("Input Row Index [FORMAT ##]  "))
                                if rowindex < len(dummydata[rowindex]):
                                    itemcounter = 0
                                    for _ in dummydata[rowindex]:
                                        itemcounter += 1
                                        
                                    row = dummydata[rowindex]
                                    print(tabulate([dummydata[rowindex]], tablefmt="github"))
                                    
                                    try:
                                        columnindex = int(input(f"Input Column Index. [0 - {itemcounter-1}]   "))
                                        while True:
                                            action = input("Input Column Action [E] Edit Column [D] Delete Column   ").lower()
                                            if action in ["e", "d"]:
                                                editrow(row, columnindex, action)
                                                break
                                            print("Invalid Input")
                                    except ValueError:
                                        pass
                            except (ValueError, IndexError):
                                print("Invalid Input")
                                pass
                else:
                    print("")
                    print("# File Not Found #".center(66, "="))
            return
        
        
        ## BROWSE MODE MAIN UI ##
        counter = 0
        for files in os.listdir(os.path.dirname(__file__)):         ## LIST ALL CSV EXTENSION FILES
            if files.endswith(".csv"):
                counter += 1
                csvfiles.append([files])
        if counter == 0:
            print("No Databases Are Found.")
            return

        while True:
            print("=".center(66, "="))
            print("")
            print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
            print("\nCurrently - Overview Mode.")
            print("")
            userinput = input("[L] Load Database [D] Delete Database [S] Search Database \n[E] Edit Database [.letmeout] Quit\n")
            magicword = userinput.replace(".", "").lower()
            if userinput.lower() == "l":
                print("=".center(66, "="))
                while True:
                    if loadBudgetData() == "Quit":
                        break
                print("")
                print("=".center(66, "="))
            if userinput.lower() == "d":
                deleteData()
                print("=".center(66, "="))
            if userinput.lower() == "s":
                print("")
                searchData()
            if userinput.lower() == "e":
                print("")
                editDatabase()
            if "letmeout" in magicword and userinput[0] == ".":     ## Triggers when csvname contains .letmeout
                return


    ## MAIN UI ##
    while True:
        print("")
        print("[ ARKY CLI BUDGET PLANNER ]".center(66, "="))
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

        if userinput == "f":
            inputDate()

        if userinput == "1":
            browseDatabase()
        elif userinput == "2":
            print("=".center(66, "="))
            print("")
            previewEntry(budget_planner)
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
            exportcsv(budget_planner)
            print("")
            pass
        elif userinput.lower() == "q":
            print("=".center(66, "="))
            print("")
            print("Quit. ^^".center(66," "))
            print("")
            exit()
