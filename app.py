"""
Mad Lib-Type Project
By Benjamin Wong
A Mad-Lib-like program school project."""

# Import statements

# Welcome the user
print("Hello user, this program here is a mad-lib used for entertainment.")
# Get user input
adjective_1 = input("Think of a random adjective:")
adjective_2 = input("Think of a word to describe a dispute:")
adjective_3 = input("Think of a first reaction you would have:")
adjective_4 = input("Think of another adjective:")
adjective_eris = input("How would you feel after not being invited to an event:")
adjective_est = input("Think of an adjective that ends with est:")
reason = input("Think of a reason for not being invited:")
noun_person1 = input("Think of a something about why a person has been abandoned:")
noun_person2 = input("Think of something someone would protect:")
verb_to = input("Think of a verb that you would do to something:")
noun = input("Think of a noun:")
noun_2 = input("Think of a noun:")
# Build narrative
story = f"The great Trojan War started with a few {adjective_1} Gods and an apple..."
story += f"During the wedding of Thetis and Peleus, the goddess of discord, Eris, was not invited for "
story += f"{reason} . Eris felt {adjective_eris} and, arriving at the wedding, tossed in the "
story += f"middle of the feast of the gods a golden apple, saying “to the {adjective_est}”. The apple "
story += f"was claimed by Hera, Athena and Aphrodite, sparking a {adjective_2} dispute among "
story += f"the three. The goddesses asked Zeus who the apple belonged to (in other words, who is "
story += f"the {adjective_est} of them all) and Zeus said that Paris, a mortal man and the rightful Prince "
story += f"of Troy, should choose."
story += f"Paris at the time was living as a shepherd on Mount Ida and was not aware of his "
story += f"divine descent. He had been abandoned as a {noun_person1}, because of an prophecy that "
story += f"said he would {verb_to} the {noun_person2} of his city. The three goddesses appeared before the "
story += f"shepherd Paris and asked him to choose who is the {adjective_est} of them all. "
story += f"Paris at first was {adjective_3}, but each of the goddesses offered him a gift: Hera offered him "
story += f"royalty and {noun}, Athena the skill of war and wisdom among men, and Aphrodite offered him the "
story += f"{adjective_4} {noun_2} in the world. Without a second, Paris gave the "
story += f"golden apple to Aphrodite. From that day on, Aphrodite was offering {noun_2} to Paris everyday. "

adjective_1 = input("Think of a random adjective:")
adjective_2 = input("Think of a word to describe a dispute:")
adjective_3 = input("Think of a first reaction you would have:")
adjective_4 = input("Think of another adjective:")
adjective_eris = input("How would you feel after not being invited to an event:")
adjective_est = input("Think of an adjective that ends with est:")
reason = input("Think of a reason for not being invited:")
noun_person1 = input("Think of a something about why a person has been abandoned:")
noun_person2 = input("Think of something someone would protect:")
verb_to = input("Think of a verb that you would do to something:")
noun = input("Think of a noun:")
noun_2 = input("Think of a noun:")
# Display results
print(story)
# Thank the user and quit
print("Thank you for using the program")