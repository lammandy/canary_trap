'''
Turning an ID to binary means email 1 is email 0 in our database. Therefore,
if 4 emails are sent, 2 line breaks are needed. 
if 5 emails are sent, 3 line breaks are needed.
If 32 emails are sent, 5 line breaks are needed.
If 33 emails are sent, 6 line breaks are needed.
'''

import math
import pprint

ids = [4, 5, 63]
ids_binary = [bin(id)[2:] for id in ids]

# Seperates paragraphs in .txt to a list.
paragraphs = []
with open('top_secret.txt', 'r', encoding="utf8") as f:
    for paragraph in f:
        paragraphs.append(paragraph.rstrip("\n"))

num_paragraphs = len(paragraphs)
paragraph_lengths = []
# for paragraph in paragraphs:
#     paragraph_lengths.append(len(paragraph))
no_matter = [paragraph_lengths.append(len(paragraph)) for paragraph in paragraphs]

# find number of line breaks needed based on emails to send
def num_lines():
    num_slots = int(input('How many emails need to be/have been sent? ')) - 1
    # ex. 65 emails sent mean we have 0-64 slots in our data. 
    # 64 = 1000000, log 2 (64) = 6 + 1 = 7
    num_lines = int(math.log(num_slots, 2)) + 1
    # the number of digits of the binary number of emails sent
    return num_lines

# Checks for the number of digits in the ID and then it's bool.

# Adds one space to the end of the paragraph based on the digit of the ID if True.
def generate_altered_document(binary_id_str):
    document = []
    idx = 0
    for paragraph in paragraphs:
        if idx < len(binary_id_str):
            if bool(int(binary_id_str[idx])):
                # 1
                paragraph += ' '
            else:
                # 0
                paragraph += '  '
        idx += 1
        document.append(paragraph)
    return document

def create_master():
    master_dict = {}
    for id in ids_binary:
        master_dict[id] = generate_altered_document(id)
        create_document(id, master_dict)
    return master_dict

def create_document(id, dict):
    with open(f"top_secret_{int(id, 2)}.txt", "w") as file:
        for paragraph in dict[id]:
            file.write(paragraph + "\n")


# TODO: read .txt file and match with binary code. Detect if the first character before linebreak is
# a space.

def read_file_list(file):
    paragraphs = []
    with open(file, 'r', encoding="windows-1252") as f:
        for paragraph in f:
            paragraphs.append(paragraph.rstrip("\n"))
    return paragraphs

def find_id(doc_list, num_lines):
    counter = 0
    id = ''
    for num in range(len(doc_list)):
        if counter < num_lines:
            diff = len(doc_list[num]) - paragraph_lengths[num]
            if diff == 1:
                id += '1'
            elif diff == 2:
                id += '0'
            else:
                pass
            counter += 1
    return id
            
    # for paragraph in doc_list:
    #     if counter < num_lines:
    #         if paragraph:
    #             last_char = paragraph[-1]
    #             print(f'Last character at the end of each paragraph is: "{last_char}"')
    #             if last_char == ' ':
    #                 try:
    #                     second_last_char = paragraph[-2]
    #                     print(f'2nd last character at the end of each paragraph is: "{second_last_char}"')
    #                     print('1')
    #                 except IndexError:
    #                     pass
    #                     print('0')
    #         else:
    #             print('empty')
    #         counter += 1

# print(read_file_list('top_secret_23.txt'))

print("Welcome to the Canary Trap text generator.")
choice = input("We have two services.\n For creating alternate versions of an email based on your employees id, press 'enter'.\n For finding out who's been leaking your secrets, type '1' and press 'enter'. ")
num_lines = num_lines()
if choice:
    file_name = input("To find the culprit, enter the file name of the leaked text: ")
    doc_list = read_file_list(file_name)
    id_binary = find_id(doc_list, num_lines)
    id = int(id_binary, 2)
    #check spaces based off of /n
    print(f"Employee {id} has been leaking your secrets!")
else:
    if num_lines <= num_paragraphs:
        print(f"Altered documents done for {ids_binary}.  Please pay $3000.")
        print(f'line breaks needed {num_lines}')
        create_master()
    else:
        print(f"Please add {num_lines - num_paragraphs} paragraphs more to proceed. \
            Any new lines will work. Thank you come again.")



