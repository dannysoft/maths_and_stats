import CMInterface as cmi
import dst_math_Interface as dsmi
import BasicStats as bs

def menuTopLevel():
    global accuracyLevel
    global numberOfQuestionSets
    accuracyLevel = 0
    numberOfQuestionSets = 1
    menuChoice = "-1"
    menuText = """
    Top Level Menu for Calc Maker.
    ==============================
    
    PRACTICE MAKES PERFECT!

    Enter 1 to show the two operands calculation menu.
    Enter 2 to show the rounding decimal numbers menu.
    Enter 3 Goto DST Math menu.
    Enter 4 to show the basic statistics menu.

    Enter 0 to Quit...
    
    """
    blnEndDemo = False
    while not blnEndDemo:
        print(menuText)
        
        validChoice = False
        while not validChoice:
            menuChoice = input("Please choose 1 to 4 [or 0 to quit]: ")
            validChoice = (menuChoice.isnumeric()) and (int(menuChoice) in range(0,8))
        #end while
            
        if menuChoice == "1":
            cmi.Twenty2operandQuestion()
        #end if
        if menuChoice == "2":
            cmi.TwentyFloatsToRound()
        #end if
        if menuChoice == "3":
            dsmi.menuDSTMath()
        #end if
        if menuChoice == "4":
            bs.menuDSTMath()
        #end if
        if menuChoice == "5":
            input("Work in progress: Press Enter to return to top level menu.")
        #end if
        if menuChoice == "6":
            input("Work in progress: Press Enter to return to top level menu.")
        #end if
        if menuChoice == "7":
            input("Work in progress: Press Enter to return to top level menu.")
        #end if
        blnEndDemo = (menuChoice == "0")
    #end while
#def end

menuTopLevel()
