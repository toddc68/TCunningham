#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# TCunningham, 2020-Feb-24, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {}
lstRow = []  # list of data row
strFileName = 'cdInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    # ------ DATA ------ #    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        lstTbl=[]
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        pass

    # ------ PROCESSING ------ #
    elif strChoice=='a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD title: ')
        strArtist = input('Enter the Artist Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        
    # ------ PRESENTATION (Input/Output) (I/O) ------ #
    elif strChoice=='i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(),sep=',')

    # ------ PROCESSING ------ #
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('Your current inventory is...')
        for row in lstTbl:
            print(*row.values(),sep=', ')
        print('CDs available to be removed: 1 through ',len(lstTbl))
        removeID=int(input('Enter an ID: '))
        magic=0
        for row in lstTbl:
            if removeID in row.values():
                #print(magic)
                del lstTbl[magic]
            else:
                magic=magic+1
        pass

    elif strChoice =='s':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow=''
            for item in row.values():
                strRow+=str(item)+','
            strRow = strRow[:-1]+ '\n'
            objFile.write(strRow)
        objFile.close()

    else:
        print('Please chose either l, a, i, d, s, or x!')
