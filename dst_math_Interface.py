import dst_math as dsm
import random as rnd


def menuDSTMath():
    blnCloseThisMenu = False
    
    while not blnCloseThisMenu:
        menuText = """
        Do some general number work
        ==========================
        
        Enter 1 To find the Highest Common Factor between two numbers.
        Enter 2 To find the Lowest Common Multiple between two numbers.
        Enter 3 To list Factors of a given number.
        Enter 4 To convert a integer value to binary.
        Enter 5 To convert a binary value to integer.
        Enter 0 to return to previous menu...
        """ 
        print(menuText)
        validChoice = False
        while not validChoice:
            menuChoice = input("Please choose 1 to 5 [or 0 to quit]: ")
            validChoice = (menuChoice.isnumeric()) and (int(menuChoice) in range(0,8))
        #end while
            
        if menuChoice == "1": whatIsHCFBetween()
        if menuChoice == "2": whatIsLCMBetween()
        if menuChoice == "3": whatAreTheFactorsOf()
        if menuChoice == "4": covertTo(True)
        if menuChoice == "5": covertTo(False)
        
        blnCloseThisMenu = (menuChoice == "0")
    #end while
#def end

def whatIsHCFBetween():
    num1 = 0
    num2 = 0
    anotherQ = True
    while anotherQ:
        numbersTheSame = True
        while numbersTheSame:
            num1 = rnd.randint(10,100) 
            num2 = rnd.randint(10,100) 
            numbersTheSame = (num1 == num2)
        #end while
        print("What is the highest common factor between {} and {}".format(num1,num2))
        hcf = int(input("Enter answer here: "))
        answer = dsm.HCF(num1,num2)
        print("Correct!") if hcf == answer else print("WRONG!:-(")
        print("Would you like to try another?")
        anotherQ = (input("Y or N: ").upper() == "Y")
    #end while
#def end
#whatIsHCFBetween()


def whatIsLCMBetween():
    num1 = 0
    num2 = 0
    anotherQ = True
    while anotherQ:
        numbersTheSame = True
        while numbersTheSame:
            num1 = rnd.randint(5,20) 
            num2 = rnd.randint(5,20) 
            numbersTheSame = (num1 == num2)
        #end while
        print("What is the lowest common multiple between {} and {}".format(num1,num2))
        lcm = int(input("Enter answer here: "))
        answer = dsm.LCM(num1,num2)
        print("Correct!") if lcm == answer else print("WRONG!:-(")
        print("Would you like to try another?")
        anotherQ = (input("Y or N: ").upper() == "Y")
    #end while
#def end
#whatIsLCMBetween()


def whatAreTheFactorsOf():
    num1 = 0
    num2 = 0
    anotherQ = True
    while anotherQ:
        numX = rnd.randint(12,200)
        instructions = """
        Below is a randomly chosen question from three types of
        'factors of' type questions,
        i.e. list all factors, what are the prime factors
        and write this number in full factor form (a product of its
        prime factors).
        """
        print(instructions)
        qtype = rnd.randint(1,3)
        print("FOR {} do the following...".format(numX))
        if qtype == 1: factors = input("Enter a comma separated list of of factors\n e.g. for 125 enter... 1, 5, 25, 125: ")
        if qtype == 2: factors = input("Enter a comma separated list of of prime factors\n e.g. for 125 enter... 5, 25: ")
        if qtype == 3: factors = input("Enter the prime factor form of the number,\n e.g. 125 = 5 x 5 x 5 x 25: ")
        answer = dsm.GetFactors(numX,qtype)
        print("You entered {}, the answer is {}".format(factors,answer))
        print("Would you like to try another?")
        anotherQ = (input("Y or N: ").upper() == "Y")
    #end while
#def end
#dsm.GetFactors(125)
#whatAreTheFactorsOf()


def covertTo(int2Bin = True):

    anotherQ = True
    while anotherQ:
        numDec = rnd.randint(8,255)
        numBin = dsm.IntToBin(numDec)
        numDec = str(numDec)
        instructions2Bin = """
        To convert integer to binary, start with the
        integer in question and divide it by 2 keeping
        notice of the quotient and the remainder. Continue
        dividing the quotient by 2 until you get a quotient
        of zero. Then just write out the remainders in the
        reverse order..
        """
        instructions2Dec = """
        The place value columns for binary numbers, going from, right to left have the following
        values: 1,2,4,8,16 etc, so the binary number 1010 has a zero value in the right most column
        which adds 0 x 1 = 0 to the over all value of the decimal equivalent, a 1 in the second
        from right column which adds 1 x 2 = 2 to the over all value of the decimal equivalent
        a zero value in the third from right column which adds 0 x 4 = 0 to the over all value of
        the decimal equivalent, and a 1 in the left most column which adds 1 x 8 = 8 to the over
        all value of the decimal equivalent.  We sum the answers to these four calculations to
        get the decimal equivalent of 1010 = 10.
        """
        print(instructions2Bin if int2Bin else instructions2Dec)
        if int2Bin:
            print("Correct!" if input("Convert {} to Binary: ".format(numDec))== numBin else "Wrong")
        else:
            print("Correct!" if input("Convert {} to Decimal: ".format(numBin))== numDec else "Wrong")
        #end if

        print("\nWould you like to try another?")
        anotherQ = (input("Y or N: ").upper() == "Y")
    #end while    
#def end
#covertTo(False)       

