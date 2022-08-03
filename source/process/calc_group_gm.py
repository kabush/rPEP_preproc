import logging
import os
import nibabel as nib
import numpy as np

from source.tools.load_subjs import *

def calc_group_gm(prm):

    logging.info('****************************************')
    logging.info(' Building Group GM mask')
    logging.info('****************************************')

    # load subjects
    subjs = load_subjs(prm)

    ## Postprocess fmriprep
    Nimg = 0
    for subj in subjs:

        subj_id = subj['id']

        print(subj['study'] + '_' + subj['name'] + ':' + subj_id)

        path = prm.path_mri_gm_mask + subj_id + '_gm_mask.nii'
        gm_img = nib.load(path)
        
        if(Nimg==0):
            grp_gm_mask_data = np.zeros(gm_img.shape)
            grp_gm_mask_data = grp_gm_mask_data + gm_img.dataobj
        else:
            grp_gm_mask_data = grp_gm_mask_data + gm_img.dataobj

        Nimg = Nimg + 1
    
    ## Binarize array for voxels having > 50% coverage
    grp_gm_mask_data[grp_gm_mask_data<round(Nimg/2)] = 0
    grp_gm_mask_data[grp_gm_mask_data>=round(Nimg/2)] = 1

    ## Create mask from array
    all_gm_img = nib.Nifti1Image(grp_gm_mask_data,gm_img.affine)

    ## Save group image
    path = prm.path_mri_gm_mask + 'group_gm_mask.nii'
    nib.save(all_gm_img,path)
    


