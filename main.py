# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited = open("./Input/Names/invited_names.txt")
# print(invited.read())
list_of_invited = invited.readlines()
print(list_of_invited)

template = open("./Input/Letters/starting_letter.txt")
letter = template.read()

for name in list_of_invited:
    invite = open(f"./Output/ReadyToSend/{name}.txt", mode="w")
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", f"{stripped_name}")
    invite.write(new_letter)

invited.close()
template.close()