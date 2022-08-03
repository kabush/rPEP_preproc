import pandas as pd
import numpy as np

def make_fd(filename):

    # This statement reads in the tsv file and creates a new dataframe in pandas ###
    df = pd.read_csv(filename, sep='\t')

    # Select wanted column in dataframe and saves it to an object###
    selected_columns = df[["framewise_displacement"]]

    # Take the object and turns it into a new dataframe
    df = selected_columns.copy()

    # Take the new data frame and turn it into a numpy array and set all na values to 0
    fd_array = df.to_numpy(na_value=0)

    # Return the fd_array back into the running script
    return(fd_array)



