###############
# Phurpa Dorji
# 02230072
#################
# REFERENCES
# @Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners. ...
# @Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming. ...
# @Chat.GPT
#################
#  Solution Score:49801
#################
# Read the input.txt file
def read_input(Input_your_file_name):  # Define a function named read_input that takes the file name as input
    x = []  # Initialize an empty list to store tuples of opponent choices and outcomes

    # Open the specified file in read mode
    with open(Input_your_file_name, 'r') as files:
        # Iterate over each line in the file
        for y in files:
            # Split the line into opponent choice and outcome based on space
            opponent_choice, outcome = y.split()
            # Append a tuple containing opponent choice and outcome to the list x
            x.append((opponent_choice, outcome))
    return x  # Return the list of tuples containing opponent choices and outcomes


# To Calculate the score for each round
def calculate_score(Total_Number_of_rounds):  # Define a function named calculate_score that takes a list of rounds as input
    Score = 0  # Initialize the total score to zero
    # Iterate over each round (opponent choice and outcome) in the list of rounds
    for opponent_choice, outcome in Total_Number_of_rounds:
        # Check the outcome of the round
        if outcome == 'X':  # If the outcome is X
            # Check the opponent's choice and update the score accordingly
            if opponent_choice == 'A':  # If opponent chose A
                Score += 3  # Add 3 to the total score
            elif opponent_choice == 'B':  # If opponent chose B
                Score += 1  # Add 1 to the total score
            elif opponent_choice == 'C':  # If opponent chose C
                Score += 2  # Add 2 to the total score
        elif outcome == 'Y':  # If the outcome is Y
            # Check the opponent's choice and update the score accordingly
            if opponent_choice == 'A':  # If opponent chose A
                Score += 4  # Add 4 to the total score
            elif opponent_choice == 'B':  # If opponent chose B
                Score += 5  # Add 5 to the total score
            elif opponent_choice == 'C':  # If opponent chose C
                Score += 6  # Add 6 to the total score
        elif outcome == 'Z':  # If the outcome is Z
            # Check the opponent's choice and update the score accordingly
            if opponent_choice == 'A':  # If opponent chose A
                Score += 8  # Add 8 to the total score
            elif opponent_choice == 'B':  # If opponent chose B
                Score += 9  # Add 9 to the total score
            elif opponent_choice == 'C':  # If opponent chose C
                Score += 7  # Add 7 to the total score
    print(f"The total score is:{Score}")  # Print the total score


# To Run the program
Input_your_file_name = "02230072/input_2_cap1.txt"  # Specify the file name to be read
calculate_score(read_input(Input_your_file_name))  # Call calculate_score function with the result of read_input function

 
