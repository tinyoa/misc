

# word_replacer
# program opens file 


import logging
import json
import os.path

logging.basicConfig(level=logging.DEBUG
                    , filename='spam.log'
                    , format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
print(logger)

f_words_map_list = 'word_mapping.json';  # file with mapping to replace
f_word_list = 'correct_words.txt';      # file with correct words to pass without check
f_output = 'output.txt';                # new, corrected file
f_text_to_check = ''                    # file to check and correct


# offer to input file for replacing worlds
f_file = input('Enter name of file with words to replace: ')
if f_file == '':
    f_file = 'words.txt' 

    

# Load mapping file 
# Ask what mode is prefered: 1. removing only words in map-file 2. ask
# Open file
    # Read file line by line
    # Each line split for words
    # if mode 1 selected then check if word in f_word_list file. Otherwise ask if word is correct
    # Check if word in f_words_map_list then replace

# loading mapping
if os.path.isfile(f_words_map_list):
    with open(f_words_map_list, "r") as file: 
        dic_mapping = json.loads(file)
else:
    dic_mapping = {}

# loading correct words
if os.path.isfile():
    with open(f_word_list, 'w') as f_correct :
        for line in f_correct:
            list_correct_words.append(line)
else:
    list_correct_words = []




#with codecs.open(filename, 'r', encoding = 'cp1252') as f_out \
#        , codecs.open(f_out_name, 'wb') as f_in: 
#    for line in f_out:
#
#        print('- -'*20)
#        f_in.write(line.encode('utf-8'))


# -- finalizing work
# saving files
with open(f_words_map_list, "w") as outfile: 
    json.dump(dic_mapping, outfile)




