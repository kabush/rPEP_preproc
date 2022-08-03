import logging
import os
import numpy as np

from source.tools.load_subjs import *
from source.tools.make_motion import *
from source.tools.make_fd import *
from source.tools.make_censor import *

def fmriprep_process_fmri(prm):

    # Initialize log section
    logging.info('****************************************')
    logging.info(' Final processing of fmriprep output')
    logging.info('****************************************')
    
    # Create sub-directory
    logging.info('Creating ' + prm.path_mri_clean)
    os.system('! mkdir ' + prm.path_mri_clean)

    # load subjs
    subjs = load_subjs(prm)

    # process subjects
    for subj in subjs:

        subj_id = subj['id']
        subj_mri_params = subj['mri_params']

        preproc = prm.mri_params[subj_mri_params]['preproc']
        tasks = prm.mri_params[subj_mri_params]['tasks']

        print(subj['study'] + '_' + subj['name'] + ':' + subj_id)
        os.system('! mkdir ' + prm.path_mri_clean + subj_id)

        # Pull top-level scan params
        for task in tasks:
            
            nscan = tasks[task]['nscan']
            print(task + ':' + str(nscan))

            for s in range(0,nscan):
    
                print('scan: ' + str(s+1))
                print('task: ' + task)
                
                fin = prm.path_fmriprep + subj_id + '/func/' + subj_id + '_task-' + task + '_desc-confounds_timeseries.tsv'
                fout_stub = subj_id + '_task-' + task
                print(fin)
                    
                # Write out preprocessing motion time-series
                motion = make_motion(fin)
                path = prm.path_mri_clean + subj_id + '/' + fout_stub + '_motion.1D'
                np.savetxt(path, motion, delimiter=' ')
                
                fd = make_fd(fin)
                path = prm.path_mri_clean + subj_id + '/' + fout_stub + '_FD.1D'
                np.savetxt(path, fd, delimiter=' ')
                
                censor = make_censor(preproc['FD_thresh'],fin)
                path = prm.path_mri_clean + subj_id + '/' + fout_stub + '_censor.1D'
                np.savetxt(path, censor, fmt='%d', delimiter=' ')                
                
                # Write out critical preprocessing variables & parameters
                with open(prm.path_tmp + 'in_path.txt', 'w') as fh:
                    fh.write(prm.path_fmriprep)
                    
                with open(prm.path_tmp + 'out_path.txt', 'w') as fh:
                    fh.write(prm.path_mri_clean)
                        
                with open(prm.path_tmp + 'subject.txt', 'w') as fh:
                    fh.write(str(subj_id))
                                
                with open(prm.path_tmp + 'task.txt', 'w') as fh:
                    fh.write(str(task))

                with open(prm.path_tmp + 'scan.txt', 'w') as fh:
                    fh.write(str(s+1))

                with open(prm.path_tmp + 'nscan.txt', 'w') as fh:
                    fh.write(str(nscan))

                with open(prm.path_tmp + 'space.txt', 'w') as fh:
                    fh.write(prm.mri_params['space'])

                with open(prm.path_tmp + 'desc.txt', 'w') as fh:
                    fh.write(prm.mri_params['desc'])

                with open(prm.path_tmp + 'fwhm.txt', 'w') as fh:
                    fh.write(str(preproc['fwhm']))

                with open(prm.path_tmp + 'temp_hz.txt', 'w') as fh:
                    fh.write(str(preproc['temp_hz']))

                # Execute the preprocessing
                os.system(prm.path_code + 'source/process/fmriprep_process_afni ' + prm.path_tmp)
                
                # Clean up tmp folder
                os.system('! rm ' + prm.path_tmp + '*.txt')
