import turtle
import pandas

IMAGE_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/025_Day/Final_Project/blank_states_img.gif" 
DATA_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/025_Day/Final_Project/50_states.csv"


# Function Declerations
def state_validiation (user_input, pandas_file, count):
    #Creating objects needed to finish tasks
    series_staes = pandas_file["state"]
    series_truth = pandas_file["T/F"]
    length_series_states = len(series_staes)

    # Global Variables and or Objects needed for function
    global states_turtle

    #Check if the user entered a valid respose checking both lower and upper case numbers
    for i in range(length_series_states):
        # First IF Getting rid of the header variable
        # Second ELIF checking if values match and state hasn't been scored before - MEANS MATCH
        # Third ELIF checkig if user_input is bad
        if(series_staes[i] == "state"):
            continue
        elif ((user_input.lower() == series_staes[i].lower()) and series_truth[i] == False): 
            x_cor = pandas_file["x"][i]
            y_cor = pandas_file["y"][i] 

            states_turtle.goto(x_cor, y_cor)
            states_turtle.write(series_staes[i])
            
            series_truth[i] = True
            count +=1
            return count 
        elif ((user_input.lower() != series_staes[i].lower()) and series_truth[i] == False): 
            continue
        elif ((user_input.lower() == series_staes[i].lower()) and series_truth[i] == True): 
           return count 
        
    return count

# Creating object using pandas to read csv data "50_states.csv"
data = pandas.read_csv(DATA_FILE_PATH)
data["T/F"] = False

# Creating objects for use
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
states_turtle = turtle.Turtle()
           

#Creating variables for use 
count_out_of_50 = 0

#Creating specfic attributes for GUI object 
my_screen.title("U.S States Game - By. Joel Lovely")
my_screen.setup(width=700, height=490)
my_screen.addshape(IMAGE_FILE_PATH)
my_turtle.shape(IMAGE_FILE_PATH)
my_turtle.penup()
states_turtle.hideturtle()
states_turtle.penup()

#Creating User Interfacce of GUI object
while count_out_of_50 != 50:
    user_input = my_screen.textinput(title=f"{count_out_of_50}/50", prompt="Guess a state name")
    if user_input == "Exit":
        break
    count_out_of_50 = state_validiation(user_input=user_input, pandas_file=data, count=count_out_of_50)

#Creating file called results.csv that has states not guessed by the user
results = []
for i in range(len(data["T/F"])):
    if(data["T/F"][i] == True):
        continue
    elif(data["T/F"][i] == False):
        results.append(data["state"][i])
        continue
results = pandas.DataFrame(results)
results.to_csv("results.csv")
    

















my_screen.exitonclick()