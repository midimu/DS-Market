import os.path


def save_dfs_to_csv(dfs, destination_directory, prefix=''):
    """
    Gets an array of DataFrames 'dfs' and stores them in the given 'destination_directory'.
    Files can have a 'prefix' added if set.
    Returns a list of directories where the stored files can be found
    """
    dir_list = []

    # transform dfs into a list if it's not
    if type(dfs) != 'list':
        dfs = [dfs]

    for df in dfs:
        # check if destination_folder exists and creates it otherwise
        if not os.path.exists(destination_directory):
            print("Creating", destination_directory, "directory")
            os.makedirs(destination_directory)
        # creating the new files
        # obtain a DatFrame name (df variable name) so the user doesn't need to input it
        df_name = [x for x in globals() if globals()[x] is df][0]
        file_path = './' + destination_directory + '/' + df_name
        if prefix:
            file_path += '_' + prefix
        file_path += '.csv'
        if not os.path.isfile(file_path):
            print(file_path, "doesn't exist. Creating new file")
        else:
            print("File already exists in", destination_directory)
            print("Overwriting file")
        df.to_csv(file_path)

        dir_list.append(file_path)
    return dir_list
