import math
import dst_math as dsm
import random as rnd

rawData = []
mean = 0

def menuDSTMath():
    blnCloseThisMenu = False
    
    while not blnCloseThisMenu:
        menuText = """
        Carry out basic statistical calculations
        ========================================
        
        Enter 1 To enter raw integer data (10 values max).
        Enter 2 To show the mean of the data entered.
        Enter 3 To show the median of the data entered.
        Enter 4 To show the maximum of the data entered.
        Enter 5 To show the minimum of the data entered.
        Enter 6 To show the standard deviation of the data entered.
        
        Enter 0 to return to previous menu...
        """ 
        print(menuText)
        validChoice = False
        while not validChoice:
            menuChoice = input("Please choose 1 to 6 [or 0 to return to previous menu]: ")
            validChoice = (menuChoice.isnumeric()) and (int(menuChoice) in range(0,8))
        #end while
            
        if menuChoice == "1": enterRawData()
        if menuChoice == "2": meanRawData()
        if menuChoice == "3": medianRawData()
        if menuChoice == "4": maxRawData()
        if menuChoice == "5": minRawData()
        if menuChoice == "6": sdRawData()
        
        blnCloseThisMenu = (menuChoice == "0")
    #end while
#def end

def enterRawData():
    global rawData
    rawData = []  #12,23,45,45,67,89,90,23,56,76]

    userInstructions = """
    To carry out the basic stats calculations in this module
    create a data set containing 10 integer values.
    """ 
    print(userInstructions)
    print("\nEnter 10 data items at the prompt...\n")
    
    for intX in range(1,11):
        validDataItem = False
        while not validDataItem:
            dataItem = input("Data: ")
            validDataItem = dataItem.isnumeric()
        #end while
        rawData.append(int(dataItem))
    #end for
    input("press <ENTER> to continue.")
#def end

def meanRawData():
    global rawData
    global mean

    if len(rawData) != 10:
        print("You must enter raw data through menu option 1")
        input("press <ENTER> to continue.")
        return
    #end for
    mean = round(sum(rawData)/10,2)
    print("\nThe mean value for the raw data you entered is: {}\n".format(mean))
    input("press <ENTER> to continue.")
#def end
    
def medianRawData():
    global rawData

    if len(rawData) != 10:
        print("You must enter raw data through menu option 1")
        input("press <ENTER> to continue.")
        return
    #end for
    
    rawData.sort()
    fithItem = rawData[4]
    sixthItem = rawData[5]
    median = (fithItem + sixthItem)/2
    print("\nThe median value for the raw data you entered is: {}\n".format(round(median,2)))
    input("press <ENTER> to continue.")
#def end

def maxRawData():
    global rawData

    if len(rawData) != 10:
        print("You must enter raw data through menu option 1")
        input("press <ENTER> to continue.")
        return
    #end for
    
    rawData.sort()
    print("\nThe maximum value for the raw data you entered is: {}\n".format(rawData[9]))
    input("press <ENTER> to continue.")
#def end

def minRawData():
    global rawData

    if len(rawData) != 10:
        print("You must enter raw data through menu option 1")
        input("press <ENTER> to continue.")
        return
    #end for
    
    rawData.sort()
    print("\nThe minimum value for the raw data you entered is: {}\n".format(rawData[0]))
    input("press <ENTER> to continue.")
#def end

def sdRawData():
    global rawData
    global mean
          
    if len(rawData) != 10:
        print("You must enter raw data through menu option 1")
        input("press <ENTER> to continue.")
        return
    #end for
    
    if mean == 0:
        print("You must enter raw data and calculate the mean through menu options 1 and 2")
        input("press <ENTER> to continue.")
        return
    #end for
    
    sumVar = 0     
    for item in rawData:
          sumVar += (item - mean)**2
    #end for
          
    sd = math.sqrt(sumVar/10)
    print("\nThe minimum value for the raw data you entered is: {}\n".format(round(sd,2)))
    input("press <ENTER> to continue.")
#def end
   
#menuDSTMath()


