import pylab

def CheckYear(date,checkYear):
    """
    Takes a string date following mm/dd/yyyy and returns true if the date is the 
    same or more recent than the checkYear. Returns false otherwise
    """
    if int(date[6:])>=checkYear:
        return True
    return False
    
def StringToInt(strList):
    """
    Takes a list of strings and returns an array of integers
    """
    #print "StringToInt run with",strList
    intNums = []
    for i in strList:
        intNums.append(int(i))
    return intNums
    
def frequencyDist(numList):
    """
    Takes an array of integers and calculates the percentage of each integer present
    """
    numMax = max(numList)
    numMin = min(numList)
    numbers = []
    frequency = []
    
    for i in range(numMin,numMax+1):
        numbers.append(i)
        count = 0
        for j in numList:
            if j== i:
                count += 1
        frequency.append((count/float(len(numList))*100))
    
    return (numbers,frequency)
   

def PowerballFreq(year=1997):
    """
    Plots all winning powerball numbers fromt he date given up to the present. 
    No input will default the year to 1997
    """    
    POWERBALL_FILE = "C:\Users\Mike\Google Drive\winnums-text.txt"
    winnums = []
    powerballNums = []
    powerplayNums = []
    
    infile = open(POWERBALL_FILE,'r',0)
    winstr=[]
    #Read the file and add each line into a string array"
    for line in infile:
        #print "Printing each line in file:",line
        winstr.append(line)
        
    #For each item in the string array of lines, split based on ' ', while ignoring the first line of the file.
    for i in range(1,len(winstr)):
            #print "String to split:",winstr[i]
            numbers = winstr[i].rstrip().split()
            #print "Split line into numbers:",numbers
            #Check if the line being tested is within the desired range, then add each number to the array of winning numbers
            if CheckYear(numbers[0],year):
                winnums += StringToInt(numbers[1:6])
                powerballNums.append(int(numbers[6]))
                #Check if powerplay was included, add to separate array
                if len(numbers)==8:
                    if int(numbers[7])==10:
                        powerplayNums.append(1)
                    else:
                        powerplayNums.append(int(numbers[7]))
    
    pylab.figure("Winnums")                
    pylab.hist(winnums,59,color="blue")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency")
    pylab.title("Winning Numbers")
    pylab.show()
    
    pylab.figure("Winnumsfreq")  
    (winnums_num,winnums_freq) = frequencyDist(winnums)              
    pylab.plot(winnums_num,winnums_freq,color="blue")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency %")
    pylab.title("Winning Numbers")
    pylab.show()
    
    pylab.figure("Powerball Winning")                
    pylab.hist(powerballNums,39,color="red")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency")
    pylab.title("Powerball Numbers")
    pylab.show()
    
    pylab.figure("Powerballfreq")  
    (powerball_num,powerball_freq) = frequencyDist(powerballNums)              
    pylab.plot(powerball_num,powerball_freq,color="red")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency %")
    pylab.title("Powerball Numbers")
    pylab.show()  
    
    pylab.figure("Powerplay Winning")                
    pylab.hist(powerplayNums,4,color="green")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency")
    pylab.title("Powerplay Numbers")
    pylab.show()
                                                                        
    pylab.figure("PowerPlayfreq")  
    (powerplay_num,powerplay_freq) = frequencyDist(powerplayNums)              
    pylab.plot(powerplay_num,powerplay_freq,color="green")
    pylab.xlabel("Numbers")
    pylab.ylabel("Frequency %")
    pylab.title("Powerplay Numbers")
    pylab.show()
                    
                

