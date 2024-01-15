import pandas
FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/026_Day/final_project/nato_phonetic_alphabet.csv"

pnemonic_data = pandas.read_csv(FILE_PATH)
pneomic_dict_data = {row.letter : row.code for index, row in pnemonic_data.iterrows()}

def phnoetic_generator():
    user_input = (input("Enter a word: ").strip()).upper() 
    try:
        pnemonic_list = [ pneomic_dict_data[char] for char in user_input]
    except KeyError:
        print("Sorry Invalid Response")
        phnoetic_generator()
    else:
        print(pnemonic_list)

phnoetic_generator()



