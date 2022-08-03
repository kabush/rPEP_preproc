import logging
import os

def clean_project(prm):

    ## Clean project directory
    logging.info('Removing ' + prm.path_pipe)
    os.system('! rm -rf ' + prm.path_pipe)
    
    ## Create project directory
    logging.info('Creating ' + prm.path_pipe + ' and all sub-directories')
    os.system('! mkdir ' + prm.path_pipe)

    ## Create tmp
    logging.info('  -Creating ' + prm.path_tmp)
    os.system('! mkdir ' + prm.path_tmp)

    ## Create top-level directories 
    logging.info('  -Creating ' + prm.path_mri)
    os.system('! mkdir ' + prm.path_mri)
