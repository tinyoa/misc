

# word_replacer
# program opens file 


import logging

logging.basicConfig(level=logging.DEBUG
                    , filename='spam.log'
                    , format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
print(logger)

f_words_map_list = '';      # file with mapping to replace
f_word_list = '';           # file with correct words

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

