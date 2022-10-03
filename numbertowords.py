unique = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
unique_ends = ('thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousand','lakh')
accessories = ('and','&')

def header():
    print("NUMBER TO WORDS")
    print("\n\n\n\n")
    
    
def getinwords():
    number = int(input("Insert your number: "))
    number_in_words = commandhandler(number)
    print(number_in_words) 

def writetofile(a,b):
    with open("output.txt","w") as external_file:
        for x in range (a,b):
            print(x,commandhandler(x),file=external_file)
    external_file.close()
    
def commandhandler(number):
    if number <= 100 : number_in_words = lessthan100(number)
    elif number <= 1000 : number_in_words = lessthan1000(number)
    elif number <= 10000 : number_in_words = lessthan10000(number)
    elif number <= 100000 : number_in_words = upto100000(number)
    return number_in_words
        

def lessthan100(num):
    number = int(num)
    number_in_words = ""
    if number <= 20: number_in_words = unique[number]
    elif number in (30,40,50,60,70,80,90,100,1000,100000):
        if number == 30: number_in_words = unique_ends[0]
        elif number == 40: number_in_words = unique_ends[1]
        elif number == 50: number_in_words = unique_ends[2]
        elif number == 60: number_in_words = unique_ends[3]
        elif number == 70: number_in_words = unique_ends[4]
        elif number == 80: number_in_words = unique_ends[5]
        elif number == 90: number_in_words = unique_ends[6]
        elif number == 100: number_in_words = unique_ends[7]
        elif number == 1000: number_in_words = unique_ends[8]
        elif number == 100000: number_in_words = unique_ends[9]
    else:
        if number > 20 and number < 30:number_in_words = unique[20] + " " + unique[number%10]
        elif number > 30 and number < 40:number_in_words = unique_ends[0] + " " + unique[number%10]
        elif number > 40 and number < 50:number_in_words = unique_ends[1] + " " + unique[number%10]
        elif number > 50 and number < 60:number_in_words = unique_ends[2] + " " + unique[number%10]
        elif number > 60 and number < 70:number_in_words = unique_ends[3] + " " + unique[number%10]
        elif number > 70 and number < 80:number_in_words = unique_ends[4] + " " + unique[number%10]
        elif number > 80 and number < 90:number_in_words = unique_ends[5] + " " + unique[number%10]
        elif number > 90 and number < 100:number_in_words = unique_ends[6] + " " + unique[number%10]
        else:number_in_words = "Invalid"
    
    return number_in_words


def lessthan1000(num):
     number = int(num)
     number_in_words = ""
     if number == 1000: number_in_words = unique_ends[8]
     elif number % 100 == 0: number_in_words= unique[int(number//100)] + " " + unique_ends[7]
     else:number_in_words = unique[int(number//100)] + " " + unique_ends[7] + " " + accessories[0] + " " + lessthan100(number%100)
     return number_in_words
 
 
def lessthan10000(num):
    number = int(num)
    number_in_words = ""
    if number == 10000: number_in_words = unique[10] + " " + unique_ends[8]
    elif number%1000 == 0: number_in_words =  unique[int(number//1000)] + " " + unique_ends[8]
    elif number%1000 < 100:number_in_words =  unique[int(number//1000)] + " " + unique_ends[8] + " " + accessories[0] + " " +  lessthan100(number%1000)
    else : number_in_words =  unique[int(number//1000)] + " " + unique_ends[8] + " " +  lessthan1000(number%1000)    
    return number_in_words
 
 
def upto100000(num):
    number = int(num)
    number_in_words = ""
    if number == 100000: number_in_words = unique[1] + " " + unique_ends[9]
    elif number%1000 == 0 : number_in_words = lessthan100(number//1000) + " " + unique_ends[8]
    elif number%1000 < 100 : number_in_words = lessthan100(number//1000) + " " + unique_ends[8] + " " + accessories[0] + " " + lessthan100(number%1000)
    else : number_in_words = lessthan100(number//1000) + " " + unique_ends[8] + " " + lessthan1000(number%1000)
    return number_in_words


# USE getinwords(YOUR_NUMBER) to get value in words
# USE writetofile(START,END) to get values between your START and END to printed to the file output.txt




    


