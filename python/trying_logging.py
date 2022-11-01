# -*- coding: utf-8 -*-
"""
trying logging

Created on Tue Nov  1 12:00:32 2022

@author: Sam


"""


# spam.log

import logging
import os

def main(name):
    
    #print(os.path.abspath(os.getcwd()))
    work_dir = os.path.dirname(os.path.abspath(__file__))
    #print(work_dir)
    
    try:
        logging.basicConfig(level=logging.DEBUG
                            , filename=work_dir +'\\spam.log'
                            , format='%(asctime)s %(clientip)-15s %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setFormatter = logging.Formatter('%(asctime)s %(clientip)-15s %(user)-8s %(message)s') 
        print('logger: ', logger)
        
        print()
        #logger.setLevel('DEBUG')
        #logging.DEBUG
        
        print('logger.level: ', logger.level)
        #10
        print()
        
        #root.format = logging.Formatter('%(asctime)s %(clientip)-15s %(user)-8s %(message)s') 
        #print('logger.format: ', logger.format)
        
        print('logger.handlers: ', logger.handlers)  
        #[<StreamHandler stderr (NOTSET)>]
        
        logger.debug('Enter in the main() function: name = ')

    #DEBUG:root:Enter in the main() function: name = oleg
    
    except Exception as e:
        print(e.__class__)
    finally:
        pass
        #logging.shutdown()

if __name__ == '__main__':
    main('petr')


#Раз, два, три, четыря. Пять


