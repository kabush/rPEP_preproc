import pandas as pd
import os
import logging

def load_subjs(prm):

    print('Loading subjects')

    map = pd.read_csv(prm.path_bids + 'participants.tsv',sep = '\t',dtype={'participant_id':str,
                                                                           'src_study_id':str})

    print(map)

    subjs = list()
    with open(prm.path_subjs + 'use_list.txt','r') as fh:

        for name in fh:

            print(name)

            name = 'sub-' + name.rstrip()

            subj_map = map.loc[map['participant_id']==name]
            subj_map = subj_map.reset_index(drop=True)
            

            participant_id = subj_map['participant_id']
            participant_id = participant_id[0]
            
            subj_src_study = 'rPEP'
            subj_src_name = participant_id
            img_format = 'NIFTI'
            mri_params = 'Philips-birc'
                
            group = subj_map['group']
            group = group[0]

            subj = dict()
            subj['id'] = participant_id
            subj['study'] = subj_src_study
            subj['name'] = participant_id
            subj['format'] = img_format
            subj['mri_params'] = mri_params
            subj['group'] = group

            subjs.append(subj)

    return(subjs)
