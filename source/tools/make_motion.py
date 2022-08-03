import pandas as pd
import numpy as np

def make_motion(filename):

    # This statement reads in the tsv file and creates a dataframe in pandas ###
    df = pd.read_csv(filename, sep='\t')
    
    # This statement gets the wanted columns in the dataframe and saves them as an object ###
    selected_columns = df[["trans_x", "trans_x_power2", "trans_x_derivative1", "trans_x_derivative1_power2",
                           "trans_y", "trans_y_power2", "trans_y_derivative1", "trans_y_derivative1_power2",
                           "trans_z", "trans_z_power2", "trans_z_derivative1", "trans_z_derivative1_power2",
                           "rot_x", "rot_x_power2", "rot_x_derivative1", "rot_x_derivative1_power2",
                           "rot_y", "rot_y_power2", "rot_y_derivative1", "rot_y_derivative1_power2",
                           "rot_z", "rot_z_power2", "rot_z_derivative1", "rot_z_derivative1_power2",
                           "csf", "csf_derivative1",
                           "white_matter", "white_matter_derivative1",
                           "global_signal", "global_signal_derivative1"]]

    # This statement takes the object selected_columns and saves it to a new dataframe
    df = selected_columns.copy()

    # Turn df1 into an array called motion with all na values set to 0
    motion_array = df.to_numpy(na_value=0)

    # Return the motion_array back into the running script
    return(motion_array)
