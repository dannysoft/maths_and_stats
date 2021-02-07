import math

def HCF(n1,n2):
    tmp = 0
    product = 0
    n1True = bool(n1)
    
    while n1True:
        # swap the items so that n1 >= n2
        if n1 < n2:
            tmp = n1
            n1 = n2
            n2 = tmp
        #end If
        # take the modulo
        n1 = n1 % n2
        n1True = bool(n1)
    #end while
    return n2
#def end
#print(HCF(150,250))

def LCM(n1,n2):
    #Public Function LCM(ByVal n1 As Long, ByVal n2 As Long) As Long
    # now n2 contains the GCD of the two numbers
    # The LCM is equal to (n1*n2) \ GCD(n1,n2)
    #print((n1 * n2))
    #print(HCF(n1, n2))
    return int((n1 * n2) / HCF(n1, n2))
#def end
#print(LCM(18,32))

def IntToBin(decnum):
    loopagain = bool(decnum)
    binval = ""
    while loopagain:
        tempbin = str(decnum % 2)
        binval = tempbin + binval

        decnum = decnum // 2
        loopagain = bool(decnum)
    #end while
    return binval
#def end
#print(IntToBin(123))

def BinToInt(binnum):
    length = len(binnum)
    runsum = 0
    #'Convert each binary digit to its corresponding integer value
    #'and add the value to the previous sum
    #'The string is parsed from the right (LSB - Least Significant Bit)
    #'to the left (MSB - Most Significant Bit)
    for i in range(1,length + 1):
        runsum = runsum + int(binnum[length-i])*2**(i-1)
    #end for
    
    return runsum    
#def end
#print(BinToInt("000101111000"))


def IsPrime(p_intNumber): #wip!!
    I = 0
    IsPrime = False
    if p_intNumber == 0 or p_intNumber == 1: 
        return False
    elif p_intNumber < 0:
        return False
    elif p_intNumber == 2:
        IsPrime = True
    elif p_intNumber % 2 == 0:
        return False
    else:
        IsPrime = True
        tmpmax = math.floor(math.sqrt(p_intNumber) + 0.5)
        for i in range(3,tmpmax,2):
            print("In IsPrime: ",p_intNumber)
            if p_intNumber % i == 0:
                IsPrime = False
                break #Exit For
            #end if
        #end for
    #end if
    return IsPrime
#def end

def CIP(num2chek): #Brute force check!
    blnIsPrime = True
    if num2chek == 1:blnIsPrime = False
    for x in range(2,num2chek):
        if (num2chek % x == 0):
            return False
    return blnIsPrime

def FullPrimeFactorForm(p_intPrimeFactors, p_intNumber):
    l_strPrimeFactorForm = ""
    l_intPowerCount = 0
    l_vrtPrimeFactor = 0

    l_strPrimeFactorForm = str(p_intNumber) + " = "
    #print("FullPrimeFactorForm ",p_intPrimeFactors)
    #return
    for l_vrtPrimeFactor in p_intPrimeFactors:
        #print("for l_vrtPrimeFactor", l_vrtPrimeFactor)
        l_intPowerCount = 1
        #print("l_vrtPrimeFactor ",l_vrtPrimeFactor)
        #return
        while (p_intNumber % (l_vrtPrimeFactor ** l_intPowerCount) == 0):
            
            l_intPowerCount = l_intPowerCount + 1
            #print("l_intPowerCount = ",l_intPowerCount)
            l_strPrimeFactorForm = l_strPrimeFactorForm + str(l_vrtPrimeFactor) + " x "
        #end while
    #end for
    l_strPrimeFactorForm = l_strPrimeFactorForm[0:len(l_strPrimeFactorForm) - 3]
    #print("inside FullPrimeFactorForm ",l_strPrimeFactorForm)
    return l_strPrimeFactorForm    
#def end

def GetFactors(p_intNumber,qtype = 1):
    l_intFactorCounter = 0
    l_intFactorCandidate = 0
    l_strFactors = ""
    l_strPrimes = ""
    l_intPrimeFactors = []
    l_intPrimeFactorsCount = 0
    p_intFactorCount = 0

    l_intFactorCandidate = 1
   
    while l_intFactorCandidate <= p_intNumber:
        if p_intNumber % l_intFactorCandidate == 0:
            if CIP(l_intFactorCandidate):
                l_intPrimeFactorsCount = l_intPrimeFactorsCount + 1
                l_intPrimeFactors.append(l_intFactorCandidate)
                l_strPrimes = l_strPrimes + " " + str(l_intFactorCandidate)
            #end If
            l_strFactors = l_strFactors + ", " + str(l_intFactorCandidate)
        #end If
        l_intFactorCandidate = l_intFactorCandidate + 1
    #end while
    if qtype == 1: return l_strFactors.replace(", ","",1)
    if qtype == 2: return l_strPrimes 
    if qtype == 3: return FullPrimeFactorForm(l_intPrimeFactors, p_intNumber)    
#def end
#print(GetFactors(169,3))
#print(CIP(1))


