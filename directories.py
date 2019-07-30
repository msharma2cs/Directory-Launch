import os
from os.path import isdir, join, exists
import sys
import shutil

# Returns the primary path.
def getPrimaryPath():
    return "/Workspace"

# Returns all the sub directories in the primary path.
def getAllSubDirectories():
    # Get the primary path
    path = getPrimaryPath()
    # Return a list of only directories, and filter out files.
    return [ f for f in os.listdir(path) if isdir(join(path, f)) ]

# Returns all the sub directories in the primary path.
def getAllSubDirectoriesForPath(path):
    # Check if path exists
    if os.path.exists(path):
        # Return a list of only directories, and filter out files.
        return [ f for f in os.listdir(path) if isdir(join(path, f)) ]
    else:
        # Return an empty list if path does not exists.
        return []
    
# Executed on click of launch event.
def launchDirectoryScript(path, directory):
    print( "Sub-directory - " + directory )
    print( "Path for selected sub-directory - " + path + "/" + directory )
    # code to execute on selected sub-directory.

    ########################################################################################
    # Be careful before uncommenting and executing this code.
    # This deletes the folder and all its contents permanently.
    # Just used it for testing.
    # Replace this piece of code with the desired script execution or actions required.
    #
    # try:
    #     shutil.rmtree(path + "/" + directory)
    # except OSError as e:
    #     print ("Error: %s - %s." % (e.filename, e.strerror))
    ########################################################################################
