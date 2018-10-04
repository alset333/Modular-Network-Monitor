#!/usr/bin/env python3
# Modular Network Monitor

# Configuration options can be found in config.py

# Built-in imports
import os
import sys
import time

# Our imports
from Utilities import eprint
from config import SharedCfg, MonitorCfg


# Function Definitions Start


def run_modules():
    for mod in MonitorCfg.MODULES:  # for "a module" in "the list of modules"
        print("Start:\t", mod)  # Announce what is starting

        modpath = os.path.normpath(cwd + "/Modules/" + mod + ".py")  # Get the module's path

        modFile = open(modpath)  # Open the module
        modContents = modFile.read()  # Read the module's contents to a variable
        modFile.close()  # Close the module

        exec(modContents)  # Execute the module's contents from the variable

        print("End:\t", mod)  # Announce what just ended


def main_loop_contents():
    print("Time:", time.time())
    run_modules()


# Function Definitions End


# Main Runner Code from here to end

cwd = sys.path[0]

outputPath = os.path.normpath(cwd + "/" + SharedCfg.OUTPUT_FOLDER_NAME)  # Get the output folder's path

if SharedCfg.DEBUG_MODE:  # Debug mode
    os.rmdir(outputPath)  # Reset output (remove output folder)

# Create the output folder or exit if it exists
try:
    os.mkdir(outputPath)  # Create the output folder
except FileExistsError:
    eprint("Error: \"", outputPath, "\" already exists.\nPlease remove or rename the existing folder.", sep="")
    exit(73)  # Allegedly 73 is EX_CANTCREAT, which seems like it would be the closest


# Main Loop
main_loop_contents()  # Run once with no starting delay

# main_loop_contents() was just run once! Since it wasn't used before now, there was never a need to declare it as 0
loopCount = 1

while MonitorCfg.LOOP_TIMES == 0 or loopCount < MonitorCfg.LOOP_TIMES:  # Left side evaluates first in Python
    # Waiting "before" (to avoid trailing sleep when finished) is possible because main_loop_contents() was run earlier
    time.sleep(MonitorCfg.LOOP_WAIT)

    loopCount += 1

    main_loop_contents()

