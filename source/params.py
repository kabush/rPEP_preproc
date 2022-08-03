base_path = '/home/kabush/'
base_name = 'rPEP'
study_list = {'rPEP'}

# Primary paths
path_code = base_path + 'workspace/code/' + base_name + '/'
path_data = base_path + 'workspace/data/' + base_name + '/derivatives/'
path_bids = base_path + 'workspace/bids/' + base_name + '/'

# Paths
path_subjs = path_code + 'subj_list/'
path_log = path_code + 'log/'
path_fmriprep = path_data + 'fmriprep/'
path_pipe = path_data + 'pipeline/'
path_tmp = path_pipe + 'tmp/'

path_mri = path_pipe + 'mri/'
path_mri_clean = path_mri + 'mri_clean/'
path_mri_gm_mask = path_mri + 'mri_gm_mask/'

# MRI sequence parameters & sequence specific preprocessing parameters
mri_params = dict()

mri_params['space'] = 'MNI152NLin2009cAsym'
mri_params['desc'] = 'preproc_bold'

mri_params['Philips-birc'] = dict()
mri_params['Philips-birc']['TR'] = 2.0
mri_params['Philips-birc']['preproc'] = dict()
mri_params['Philips-birc']['preproc']['fwhm'] = 8.0
mri_params['Philips-birc']['preproc']['temp_hz'] = 0.0078
mri_params['Philips-birc']['preproc']['FD_thresh'] = 0.5
mri_params['Philips-birc']['preproc']['gm_prob'] = 0.7
mri_params['Philips-birc']['tasks'] = dict()
mri_params['Philips-birc']['tasks']['identify1'] = dict({'nscan': 1, 'vols': 166})
mri_params['Philips-birc']['tasks']['identify2'] = dict({'nscan': 1, 'vols': 166})
mri_params['Philips-birc']['tasks']['modulate1'] = dict({'nscan': 1, 'vols': 228})
mri_params['Philips-birc']['tasks']['modulate2'] = dict({'nscan': 1, 'vols': 228})
