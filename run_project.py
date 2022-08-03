## ========================================
## ========================================
## 
##  Keith Bush, PhD (2021)
##  Univ. of Arkansas for Medical Sciences
##  Brain Imaging Research Center (BIRC)
## 
## ========================================
## ========================================

import logging
from time import gmtime, strftime

import source.params as prm
import source.clean as cln

from source.process.fmriprep_process_fmri import *
from source.process.fmriprep_process_gm import *

def main():

    # ----------------------------------------
    # Set-up logging
    time_str = strftime('%Y_%b_%d_%H:%M:%S', gmtime())
    log_file = prm.path_log + time_str + '_log.txt'
    logging.basicConfig(filename=log_file, level=logging.INFO)

    # ----------------------------------------
    # Clear and reconstruct the project data folder
    cln.clean_project(prm)
    
    # ----------------------------------------
    # Post-processing fmriprep outputs
    fmriprep_process_fmri(prm) # Final process after fmriprep
    fmriprep_process_gm(prm)   # Extract grey matter masks
    
if __name__ == '__main__':
    main()
