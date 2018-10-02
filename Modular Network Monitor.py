#!/usr/bin/env python3
# Modular Network Monitor

# Configuration options can be found in config.py

# Built-in imports
import os
import sys

# Our imports
from Utilities import eprint
from config import SharedCfg, MonitorCfg

cwd = sys.path[0]

outputPath = os.path.normpath(cwd + "/" + SharedCfg.OUTPUT_FOLDER_NAME)  # Get the output folder's path

# Create the output folder or exit if it exists
try:
    os.mkdir(outputPath)  # Create the output folder
except FileExistsError:
    if SharedCfg.DEBUG_MODE:
        os.rmdir(outputPath)
        os.mkdir(outputPath)  # Create the output folder
    else:
        eprint("Error: \"", outputPath, "\" already exists.\nPlease remove or rename the existing folder.", sep="")
        exit(73)  # Allegedly 73 is EX_CANTCREAT, which seems like it would be the closest


for mod in MonitorCfg.MODULES:  # for "a module" in "the list of modules"
    print("Start:\t", mod)  # Announce what is starting

    modpath = os.path.normpath(cwd + "/Modules/" + mod + ".py")  # Get the module's path

    modFile = open(modpath)  # Open the module
    modContents = modFile.read()  # Read the module's contents to a variable
    modFile.close()  # Close the module

    exec(modContents)  # Execute the module's contents from the variable

    print("End:\t", mod)  # Announce what just ended
