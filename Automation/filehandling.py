# test1

'''
# Creating and Writing to a File
file_name = 'bot.txt'
content = "assistant bot commands and maintenance"

# Open the file in write mode
with open(file_name, "w") as file:
    file.write(content)

# Reading from a File
with open(file_name, "r") as file:
    read_content = file.read()
    print(read_content)

# Appending to a File
additional_content = "\nensure to check the manual incase of any level 1-10 problem"

# Open the file in append mode
with open(file_name, "a") as file:
    file.write(additional_content)

# Reading from the File Again
with open(file_name, "r") as file:
    read_content = file.read()
    print(read_content)

'''

# test2

file_name = "networksockets.txt"
content = "RouterInstructions"

with open(file_name, "w") as file:
    file.write(content)

# reading line by line

with open(file_name, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Strip newline character

additional_content = "\nConfirm your IP address."

with open(file_name, "a") as file:
    file.write(additional_content)

with open(file_name, "r") as file:
    read_content = file.read()
    print(read_content)
    
