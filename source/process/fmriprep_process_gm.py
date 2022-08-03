import logging
import os

from source.tools.load_subjs import *
from source.process.calc_group_gm import *

def fmriprep_process_gm(prm):

    logging.info('****************************************')
    logging.info(' Building GM masks')
    logging.info('****************************************')

    #Create sub-director
    logging.info('Removing ' + prm.path_mri_gm_mask)
    os.system('rm -rf ' + prm.path_mri_gm_mask)
    logging.info('Creating ' + prm.path_mri_gm_mask)
    os.system('mkdir ' + prm.path_mri_gm_mask)

    # load subjects
    subjs = load_subjs(prm)

    ## Postprocess fmriprep
    for subj in subjs:

        subj_id = subj['id']
        subj_mri_params = subj['mri_params']
        preproc = prm.mri_params[subj_mri_params]['preproc']
        print(subj['study'] + '_' + subj['name'] + ':' + subj_id)

        # write processing information to tmp for afni code
        with open(prm.path_tmp + 'in_path.txt','w') as fh:
            fh.write(prm.path_fmriprep)
        
        with open(prm.path_tmp + 'template_path.txt','w') as fh:
            fh.write(prm.path_mri_clean)

        with open(prm.path_tmp + 'out_path.txt','w') as fh:
            fh.write(prm.path_mri_gm_mask)

        with open(prm.path_tmp + 'subject.txt','w') as fh:
            fh.write(subj_id)

        with open(prm.path_tmp + 'space.txt','w') as fh:
            fh.write(prm.mri_params['space'])

        with open(prm.path_tmp + 'gm_prob.txt','w') as fh:
            fh.write(str(preproc['gm_prob']))

        # process the mask
        os.system('! ' + prm.path_code + 'source/process/gm_mask_process_afni ' + prm.path_tmp)
        
        # clean-up
        os.system('! rm ' + prm.path_tmp + '*')

    ## Calc Group GM mask
    calc_group_gm(prm)
