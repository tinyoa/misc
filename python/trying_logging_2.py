# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:17:41 2022

@author: Sam
"""



# spam.log



import logging

logging.basicConfig(level=logging.DEBUG
                    , filename='spam.log'
                    , format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
print(logger)

print()
#logger.setLevel('DEBUG')
#logging.DEBUG

print(logger.level)     
#10
print()

print(logger.handlers)  
#[<StreamHandler stderr (NOTSET)>]

def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    #DEBUG:root:Enter in the main() function: name = oleg

if __name__ == '__main__':
    main('kirll')

