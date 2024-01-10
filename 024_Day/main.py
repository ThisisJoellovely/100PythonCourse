import os 

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
STARTING_LETTER = "/Users/lovely/Documents/100_DaysOfProgramming/024_Day/Input/Letters/starting_letter.txt"
DESTINATION_LETTER = "/Users/lovely/Documents/100_DaysofProgramming/024_Day/Ouput/ReadyToSend"
NAMES_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/024_Day/Input/Names/invited_names.txt"

#Global Variables 
names = []

def create_letter(filename ,name):
    """"This Function will take the parameter of a name and pass name into subjgated letter and create a file and set in the output file"""        
    file_path = DESTINATION_LETTER + filename
    with open(STARTING_LETTER) as file:
        header = file.readline(11)
        header.replace("[name]" , name)
        content = file.read()  
        with open(file_path,"w") as export:
            export.write(header)
            export.write(content)

def get_names(filename):
    """This is going retrive lists and add to a global list defined in the main program"""
    global names
    with open(filename) as file:
        while file.closed != True:
            content = file.readlines()
            names.append(content)

get_names(NAMES_PATH)
for i in range(len(names)):
    current_name = names[i]
    filename = "Finished_" + current_name
    create_letter(filename , current_name)
print("Finished")



