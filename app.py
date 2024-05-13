"""
Mad Lib-Type Project
By Benjamin Wong
A Mad-Lib-like program school project.
"""

# Import statements

# Clearing the Screen

# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 
# sleep for 1 seconds after printing output
sleep(1)
 
# now call function we defined above
clear()

# Welcome the user
print("Hello user, this program here is a mad-lib used for entertainment.")

# Get user input
adjective_1 = input("Think of a random adjective:")
clear()
adjective_2 = input("Think of a word to describe a dispute:")
clear()
adjective_3 = input("Think of a first reaction you would have:")
clear()
adjective_4 = input("Think of another adjective:")
clear()
adjective_eris = input("How would you feel after not being invited to an event:")
clear()
adjective_est = input("Think of an adjective that ends with est:")
clear()
reason = input("Think of a reason for not being invited:")
clear()
noun_person1 = input("Think of a something about why a person has been abandoned:")
clear()
noun_person2 = input("Think of something someone would protect:")
clear()
verb_to = input("Think of a verb that you would do to something:")
clear()
noun = input("Think of a noun:")
clear()
noun_2 = input("Think of another noun:")
clear()

# Build narrative
start = input("hit enter to begin\n")
clear()
story = f"\tThe great Trojan War started with a few {adjective_1} Gods and an apple... \n"
story += f"During the wedding of Thetis and Peleus, the goddess of discord, Eris, was not invited for {reason}. \n" 
story += f"Eris felt {adjective_eris} and, arriving at the wedding, tossed in the \n"
story += f"middle of the feast of the gods a golden apple, saying “to the {adjective_est}”. \n"
story += f"The apple was claimed by Hera, Athena and Aphrodite, sparking a {adjective_2} dispute among the three. \n"
story += f"The goddesses asked Zeus who the apple belonged to (in other words, who is- \n"
story += f"the {adjective_est} of them all) and Zeus said that Paris, a mortal man and the rightful Prince of Troy, should choose.\n"
story += f"Paris at the time was living as a shepherd on Mount Ida and was not aware of his divine descent.\n"
story += f"He had been abandoned as a {noun_person1}, because of an prophecy that said he would {verb_to} the {noun_person2} of his city.\n"
story += f"The three goddesses appeared before the shepherd Paris and asked him to choose who is the {adjective_est} of them all. \n"
story += f"Paris at first was {adjective_3}, but each of the goddesses offered him a gift: Hera offered him royalty and {noun},\n"
story += f" Athena the skill of war and wisdom among men, and Aphrodite offered him the most {adjective_4} {noun_2} in the world. \n"
story += f"Without a second, Paris gave the golden apple to Aphrodite. From that day on, Aphrodite was offering {noun_2} to Paris everyday. "

# Display results
print(story)

# Thank the user and quit
print("\nThank you for using the program.")   