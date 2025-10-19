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
    print(pyfiglet.figlet_format("kitty", font="alligator", justify="center", width=68))         ## STARTUP ASCII ART

    if os.getcwd() != os.path.dirname(__file__):
        os.chdir(os.getcwd()+"/goober")
    
    tempDatabase = []
    
    
    
    ## LOOKS FOR THE KEYWORD "".LETMEOUT" ON EVERY INPUT ##
    def letmeout(userinput):
        if userinput.lower() in [".letmeout"]:
            return True
        return False



    ## SORT DATABASE ##
    def sortDatabase(data, values, location):
        print("=".center(66, "="))
        print("")
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
                print("")
                if userinput.lower() == "a":
                    mode = "Account"
                    return mode
                elif userinput.lower() == "d":
                    sortingdate = True
                    df["Date"] = pd.to_datetime(df["Date"], format="%Y.%m.%d")
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
                print("")
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
            sorted_df["Date"] = sorted_df["Date"].dt.strftime("%Y.%m.%d")

        values = []
        for i in range(0, len(data)):
            values.append(int(data[i][2]))

        print(f"# Sorted Records By {mode} [{order}] Within {location} #".center(66, "="))
        print("")
        print(tabulate(sorted_df, headers=["Type","Description","Account","Date","Category"], tablefmt="pipe", showindex=False))
        userinput = input(f"\n\033[4m Total Spent. { sum(values) }\033[24m ___________________ [Press Enter To Quit.]  ")
        return
    
    
    
    ## DISPLAY ADDED RECORDS ##
    def previewEntry(tempDatabase):
        headers = ["Type","Description","Account","Date","Category"]
        data = []
        values = []
        for i in range(1, len(tempDatabase)):
            tempDatabase[i][2] = int(tempDatabase[i][2])
            data.append(tempDatabase[i])
            values.append(tempDatabase[i][2])

        print("# Database Preview #".center(66, "_"))
        print("")
        print(tabulate(data, headers=headers, tablefmt="pipe"))
        while True:
            userinput = input(f"\n\033[4m Total Spent. { sum(values) }\033[24m _______________ [S] Sort [Press Enter To Quit.]  ").lower()
            if userinput == "s":
                print("")
                sortDatabase(data, values, "Database")
                return
            return



    ## ADD NEW RECORDS TO NEW CSV FILE ##
    def addDatabase():

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
                userinput = input("Enter Entry Type. [I] Income [E] Expenses [.letmeout] Quit   ")
                print("")
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
                userinput = input("Enter Account. [.letmeout] Quit   ")
                print("")
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
                print("")
                if letmeout(userinput) == True:
                    return("Quit")

                if validate(userinput) == True:
                    print("_".center(66, "_"))
                    new_table.append(userinput)
                    break
                print("\nInvalid Date.")
                print("_".center(66, "_"))

            ## ENTER CATEGORY ##
            while True:
                userinput = input("Enter Category. [U] Utilities [T] Transport [R] Rent [F] Food \n[S] Shopping [.letmeout] Quit   ")
                print("")
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
                print("")
                if userinput.lower() == "y":
                    tempDatabase.append(new_table)
                    while True:
                        userinput = input("Add Another Entry? [Y] Yes [N] No   ")
                        print("")
                        while True:
                            if userinput.lower() == "y":
                                print("=".center(66, "="))
                                return
                            elif userinput.lower() == "n":
                                print("# Database Created #".center(66, "_"))
                                print("")
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
    def exportcsv(tempDatabase):
        while True:
            userinput = input("Input Filename. [.letmeout] Quit\n\n")
            print("")
            if letmeout(userinput) == True:
                return

            while True:
                if userinput == "":
                    print("Filename Is Missing.")
                    print("_".center(66, "_"))
                    break
                else:
                    userinput = userinput+".csv"
                    confirm = input("Confirm Filename? [Y] Yes [N] No   ").lower()
                    print("")
                    if confirm == "y":
                        if os.path.exists(userinput):
                            while True:
                                confirm = input("Filename Exists. [O] Overwrite [P] Push   ").lower()
                                print("")
                                if confirm == "o":
                                    with open(userinput, "w", newline="") as file:
                                        tempDatabase.insert(0, ["Type","Description","Account","Date","Category"])
                                        writer = csv.writer(file)
                                        writer.writerows(tempDatabase)
                                        return

                                if confirm == "p":
                                    with open(userinput, "a", newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(tempDatabase)
                                        return

                        else:
                            with open(userinput, "w", newline="") as file:
                                tempDatabase.insert(0, ["Type","Description","Account","Date","Category"])
                                writer = csv.writer(file)
                                writer.writerows(tempDatabase)
                            print("# File Exported #".center(66,"_"))
                        return
                    if confirm == "n":
                        print("_".center(66, "_"))
                        break            


    ## BROWSING DIRECTORY CSVS ##
    def browseDatabase():
        csvfiles = []

         ## LOADING MODE ##
        def loadBudgetData():
            print("=".center(66, "="))
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Loading Mode")
                print("")
                userinput = str(input("Input Filename. [FORMAT ######]  [.letmeout] Quit\n"))
                if letmeout(userinput) == True:
                    return "Quit"
                
                filename = userinput+".csv"
                headers = ["Type","Description","Account","Date","Category"]
                data = []
                values = []

                if os.path.exists(filename):
                    with open(filename, "r") as file:
                        reader = csv.reader(file)
                        list_of_rows = list(reader)

                        for i in range(1, len(list_of_rows)):
                            data.append(list_of_rows[i])
                            values.append(int(list_of_rows[i][2]))

                    if len(data) == 0:
                        print("# Empty Database #".center(66, "="))
                    else:
                        print("")
                        print("# Loading CSV Data #".center(66, "_"))
                        print("")
                        print(tabulate(data, headers=headers, tablefmt="pipe"))
                        while True:
                            userinput = input(f"\n\033[4m Total Spent. { sum(values) }\033[24m ____________ [S] Sort [R] Return [Q] Quit  ") .lower()
                            print("")
                            if userinput == "s":
                                sortDatabase(data, values, filename)
                                print("")
                                return
                            elif userinput == "q":
                                return "Quit"
                            elif userinput == "r":
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
                userinput = str(input("Input Filename. [FORMAT ######] [.letmeout] Quit\n"))
                print("")
                if letmeout(userinput) == True:
                    return
                
                userinput = userinput + ".csv"
                while True:
                    confirm = input("Confirm Filename? [DELETION CANNOT BE REVERTED.] [Y] Yes [N] No  ").lower()
                    print("")
                    if confirm == "y":
                        if os.path.exists(userinput):
                            for item in csvfiles:
                                for name in item:
                                    if name == userinput:
                                        csvfiles.remove(item)

                            os.remove(userinput)
                            print("# Database Removed #".center(66, "="))
                            break
                        else:
                            print("# File Not Found #".center(66, "="))
                            break
                    if confirm == "n":
                        print("_".center(66, "_"))
                        break
                    print("Invalid Input.")
                    print("")



        ## SEARCH MODE ##
        def searchData():

            ## GLOBAL SEARCH ##
            def globalSearch():
                while True:
                    print("=".center(66, "="))
                    print("")
                    userinput = input("Input Keyword/Value. [D] Disable Global Search [S] Sort Directory \n\n")
                    print("")
                    if userinput.lower() == "d":
                        print("=".center(66, "="))
                        return
                    
                    filenames = []
                    headers = ["Type","Description","Account","Date","Category"]
                    data = []
                    values = []
                    matchedrecord = []
                    matchedvalues = []

                    for files in os.listdir(os.path.dirname(__file__)):
                        if files.endswith(".csv"):
                            filenames.append(files)

                    for stuff in filenames:
                        with open(stuff, "r") as file:
                            reader = csv.reader(file)
                            list_of_rows = list(reader)
                            for i in range(1, len(list_of_rows)):
                                    list_of_rows[i][2] = int(list_of_rows[i][2])
                                    data.append(list_of_rows[i])
                                    values.append(list_of_rows[i][2])

                        for record in list_of_rows:
                            for item in record:
                                if str(item) == userinput:
                                    try:
                                        matchedvalues.append(int(record[2]))
                                    except ValueError:
                                        break
                                    matchedrecord.append(record)

                    if userinput.lower() == "s":
                        sortDatabase(data, values, "Directory")
                        print("")
                    else:
                        if len(matchedrecord) == 0:
                            print("No Matching Results.")
                        else:
                            print("# Search Result Within All Directory #".center(66, "="))
                            print("")
                            print(tabulate(matchedrecord, headers=headers, tablefmt="pipe"))
                            userinput = input(f"\n\033[4m Total Spent. { sum(matchedvalues) }\033[24m ______________ [S] Sort [Press Enter To Quit.]  ").lower()
                            if userinput == "s":
                                print("")
                                sortDatabase(matchedrecord, matchedvalues, "Directory")
                            print("")



            ## MAIN FILE SEARCH ##
            print("=".center(66, "="))
            while True:
                ## CHECKS WHETHER FILE EXISTS ##
                while True:
                    print("")
                    print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                    print("\nCurrently - Search Mode.")
                    print("")

                    userinput = str(input("Input Filename. [FORMAT ######] [G] Global Search [.letmeout] Quit\n"))
                    if letmeout(userinput) == True:
                        print("")
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

                           ## GRABS ALL DATA FROM DATABASE ##
                            with open(filename, "r") as file:
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
                                print("=".center(66, "="))
                                print("")
                                userinput = str(input(f"Input Keyword/Value. [Currently In {filename}] [.letmeout] Quit \n\n"))
                                print("")
                                if letmeout(userinput) == True:
                                    print("=".center(66, "="))
                                    break

                                matchedrecord = []
                                matchdvalues = []

                                for record in data:
                                    for item in record:
                                        if str(item) == userinput:
                                            record[2] = int(record[2])
                                            matchedrecord.append(record)
                                            matchdvalues.append(int(record[2]))

                                if len(matchedrecord) == 0:
                                    print("No Matching Results.")
                                else:
                                    print(f"# Search Results In {filename} #".center(66, "="))
                                    print("")
                                    print(tabulate(matchedrecord, headers=headers, tablefmt="pipe"))
                                    userinput = input(f"\n\033[4m Total Spent. { sum(matchdvalues) }\033[24m __________ [S] Sort [Press Enter To Quit.]  ")

                                    if userinput.lower() == "s":
                                        print("")
                                        sortDatabase(matchedrecord, matchdvalues, filename)
                                    print("")
                        else:
                            print("# File Not Found #".center(66, "="))



        ## EDIT DATABASE ##
        def editDatabase():
            newdata = [["Type","Description","Account","Date","Category"]]
            editstate = False
            
             ## EDIT ROW ##
            def editrow(row, columnindex):
                def swapItem(userinput):
                    if columnindex == 0:
                        if userinput == "i":
                            row[2] = str(abs(int(row[2])))
                            return "Income"
                        if userinput == "e":
                            row[2] = str(-abs(int(row[2])))
                            return "Expenses"
                    if columnindex == 2:
                        try:
                            return int(userinput)
                        except ValueError:
                            pass
                    if columnindex == 3:
                        try:
                            if 1677 < (datetime.strptime(userinput, "%Y.%m.%d").year) < 2262:
                                return userinput
                        except ValueError:
                            pass
                    if columnindex == 4:
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
                
                ## IF TYPE COLUMN ##
                if columnindex == 0:
                    while True:
                        userinput = input("Enter New Entry Type. [I] Income [E] Expenses [.letmeout] Quit   ").lower()
                        if letmeout(userinput) == True:
                            return row
                        if swapItem(userinput) != "Invalid":
                            row[columnindex] = swapItem(userinput)
                            break
                        else:
                            print("")
                            print("Invalid Input.")
                            print("")
                
                ## IF DESCRIPTION COLUMN ##
                if columnindex == 1:
                    while True:
                        userinput = input("Enter New Description. [Enter To Leave Blank] [.letmeout] Quit\n")
                        if letmeout(userinput) == True:
                            return row
                        row[columnindex] = userinput
                        break
                            
                ## IF ACCOUNT COLUMN ##
                if columnindex == 2:
                    while True:
                        userinput = input("Enter New Account. [.letmeout] Quit   ")
                        if letmeout(userinput) == True:
                            return row
                        if swapItem(userinput) != "Invalid":
                            row[columnindex] = swapItem(userinput)
                            break
                        else:
                            print("")
                            print("Invalid Input.")
                            print("")

                ## IF DATE COLUMN ##
                if columnindex == 3:
                        while True:
                            userinput = input("Enter New Date. [FORMAT YYYY.MM.DD [1678 - 2261]] [.letmeout] Quit   ")
                            if letmeout(userinput) == True:
                                return row
                            if swapItem(userinput) != "Invalid" and len(userinput) == 10:
                                row[columnindex] = swapItem(userinput)
                                break
                            else:
                                print("")
                                print("Invalid Input.")
                                print("")
                            
                ## IF CATAGORY COLUMN ##
                if columnindex == 4:
                    while True:
                        userinput = input("Enter New Category. [U] Utilities [T] Transport [R] Rent [F] Food [S] Shopping \n[.letmeout] Quit   ").lower()
                        if letmeout(userinput) == True:
                            return row
                        if swapItem(userinput) != "Invalid":
                            row[columnindex] = swapItem(userinput)
                            break
                        else:
                            print("")
                            print("Invalid Input.")
                            print("")
                
                print("")
                print(f"# Edited Row {rowindex} Preview #".center(66, "_"))
                print("")
                print(tabulate([row], headers="keys", tablefmt="github", colalign=("center", "center", "center", "center", "center")))
                return row

            print("=".center(66, "="))
            while True:
                print("")
                print(tabulate(csvfiles, headers=["# Databases Found Within Directory #".center(60, " ")], tablefmt="github"))
                print("\nCurrently - Edit Mode.")
                print("")
                userinput = str(input("Input Filename. [FORMAT ######] [.letmeout] Quit\n"))
                if letmeout(userinput) == True:
                    return
                print("")

                userinput = userinput+".csv"
                if os.path.exists(userinput):
                    dummydata = []

                    with open(userinput, "r") as file:
                        reader = csv.reader(file)
                        list_of_rows = list(reader)
                        for i in range(1, len(list_of_rows)):
                            dummydata.append(list_of_rows[i])

                    if len(dummydata) == 0:
                        print("# Empty Database #".center(66, "="))
                    else:
                        while True:
                            try:
                                print(f"# {userinput} Database Preview #".center(66, "_"))
                                print("")
                                print(tabulate(dummydata, headers=["Type","Description","Account","Date","Category"], tablefmt="pipe", showindex=True))
                                print("")

                                rowindex = input(f"Input Row Index [0 - {len(dummydata)-1}] [.letmeout] Quit   ")
                                if letmeout(rowindex) == True:
                                    print("")
                                    print("=".center(66, "="))
                                    break
                                rowindex = int(rowindex)
                                
                                if 0 <= rowindex < len(dummydata[rowindex]) and isinstance(rowindex, int): 
                                    row = dummydata[rowindex]
                                    headers = []
                                    counter = 0
                                    for _ in row:
                                        headers.append((counter))
                                        counter += 1
                                    
                                    print("")
                                    print(f"# Row {rowindex} Preview #".center(66, "_"))
                                    print("")
                                    print(tabulate([dummydata[rowindex]], headers="keys", tablefmt="github", colalign=("center", "center", "center", "center", "center")))
                                    print("")
                                   
                                    while True: 
                                        try:
                                            columnindex = input(f"Input Column Index. [0 - 4] [D] Delete Row {rowindex} [.letmeout] Quit   ")
                                            print("")
                                            if letmeout(str(columnindex)) == True:
                                                break
                                            if columnindex.lower() == "d":
                                                while True:
                                                    confirm = input("Confirm Deletion? [Y] Yes [N] No   ").lower()
                                                    print("")
                                                    if confirm == "y":
                                                        dummydata.pop(rowindex)
                                                        editstate = True
                                                    if confirm == "n":
                                                        break
                                                    print("Invalid Input.")
                                                    print("")
                                            else:
                                                columnindex = int(columnindex)
                                                if 0 <= columnindex <= 4 and isinstance(columnindex, int):
                                                    while True:
                                                        try:
                                                            if dummydata[rowindex] != editrow(row, columnindex):
                                                                dummydata[rowindex] = editrow(row, columnindex)
                                                                editstate = True
                                                            print("")
                                                            break
                                                        except ValueError:
                                                            print("Invalid Input.")
                                                            print("")
                                                            pass
                                                else:
                                                    print("Invalid Input.")
                                                    print("")
                                        except ValueError:
                                            print("Invalid Input.")
                                            print("")
                                                
                            except (ValueError, IndexError):
                                print("")
                                print("Invalid Input.")
                                print("")
                                pass


                        ## OVERWRITES FILE ##
                        for item in dummydata:
                            newdata.append(item)
                        if editstate != False:
                            while True:
                                userinput = input("Save Changes? [Y] Yes [N] No   ").lower()
                                if userinput == "y":
                                    with open(filename, "w", newline="") as file:
                                        writer = csv.writer(file)
                                        writer.writerows(newdata)
                                    return
                                if userinput == "n":
                                    return
                                print("Invalid Input.")
                                print("")
                else:
                    print("# File Not Found #".center(66, "="))
            return
        
        
        
        ## BROWSE MODE MAIN UI ##
        counter = 0
        ## LIST ALL CSV EXTENSION FILES ##
        for files in os.listdir(os.path.dirname(__file__)):
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
            userinput = input("[L] Load [D] Delete [S] Search [E] Edit [.letmeout] Quit   ")
            print("")
            if letmeout(userinput) == True:
                return
            if userinput.lower() == "l":
                while True:
                    if loadBudgetData() == "Quit":
                        break
                print("")
            if userinput.lower() == "d":
                deleteData()
            if userinput.lower() == "s":
                searchData()
            if userinput.lower() == "e":
                print(tabulate(editDatabase(), tablefmt="pipe"))



    ## MAIN UI ##
    while True:
        print("")
        print("[ KITTY CLI BUDGET PLANNER ]".center(66, "="))
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
            previewEntry(tempDatabase)
            pass
        elif userinput == "3":
            print("=".center(66, "="))
            while True:
                if addDatabase() == "Quit":
                    break
            pass
        elif userinput == "4":
            print("=".center(66, "="))
            exportcsv(tempDatabase)
            print("")
            pass
        elif userinput.lower() == "q":
            print("=".center(66, "="))
            print("")
            print("Quit. ^^".center(66," "))
            print("")
            exit()
