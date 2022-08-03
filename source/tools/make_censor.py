## Code adapted from Maegan Calvert's rPEP project code

import pandas as pd
import numpy as np

def make_censor(FD_thresh, filename):

    # This statement reads in the tsv file and creates a new dataframe in pandas
    df = pd.read_csv(filename, sep='\t')

    # Select wanted column in dataframe and saves it to an object
    selected_columns = df[["framewise_displacement"]]

    # Take the object and turns it into a new dataframe ###
    df = selected_columns.copy()

    # Take the new data frame and turn it into a numpy array and set all na values to 0
    x = df.to_numpy(na_value=0)

    # Take the numpy array x and compare the values in p.param_mri_FD_thresh. 
    # This will return a Boolean value
    y = np.array(x <= FD_thresh)

    # Need to change the Boolean value into 0's and 1's and save into a different array
    z = (1 * y)  # changing True = 0 and False = 1

    # Create z as an integer rather than a float
    zint = []
    for num in z:
        zint.append(np.int(num))

    # Copy array into a tmp object so that we are not iterating over and changing values
    # in the same array
    tmp_z = np.array(zint)

    # Iterate over each item in the z array. For each item in the array, val = item. 
    # If val = 0 then the next item also needs to be
    ### equal to 0. If not, continue ###
    for i in range(0, len(zint) - 1):  # np.array(z))-1):
        val = zint[i]
        if val == 0:
            tmp_z[i + 1] = 0
        else:
            continue

    # save temporary object back as original object
    zint = tmp_z

    # Also need to look at the differences between items. Outdiff are the differences 
    # between items in the z array. (np.diff) function

    # allows us to do this without calculating by hand
    outdiff = np.diff(zint)
    
    # Need to copy the outdiff array into a temporary object so that we are not iterating
    # over and changing values in the same array
    temp_outdiff = np.array(zint)

    # Iterate over each item in the outdiff array. v1-v5 are objects that define specific 
    # items in the array. For each item in the array,
    
    # if special cases arise then set those cases to 0. This prevents any singleton values.
    for u in range(0, len(outdiff) - 2):
        v1 = outdiff[u]
        v2 = outdiff[u + 1]
        v3 = outdiff[u + 2]
        v4 = outdiff[-1]
        v5 = outdiff[-2]
        if v1 == -1 and v2 == 1:
            temp_outdiff[u] = 0
        elif v1 == 1 and v2 == -1:
            temp_outdiff[u] = 0
        elif v1 == 0 and v2 == 1 and v3 == 0:
            temp_outdiff[u + 1] = 0
        elif v4 == 1 and v5 == 0:
            temp_outdiff[-1] = 0
        else:
            continue
    
    # save the temporary array as the original array
    zint = temp_outdiff
    # save the original array as a name that will make sense to others (and is related 
    # to the function
    censor_array = zint
    censor_array.astype(int)

    # Return the censor_array back into the running script
    return(censor_array)
