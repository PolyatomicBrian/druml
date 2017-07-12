#!/usr/bin/env python

"""
druml.py: Generates a Unified Modeling Language (UML) file and a Class Diagram
          (PNG) for each Drupal Project in a directory.

Usage:
        $ python druml.py -p /PATH/TO/PROJECTS/
"""

__author__    = "Brian Jopling"
__copyright__ = "Copyright 2017, University of Pennsylvania School of " \
                "Arts and Sciences."
__credits__   = ["Brian Jopling", "Clay Wells"]
__license__   = "GNU GENERAL PUBLIC LICENSE"
__version__   = "1.0.0"
__status__    = "Development"


""" IMPORTS """
# Used for getting args.
from optparse import OptionParser
# Used for getting list of project folders.
import os
# Used for running bash commands.
import subprocess


""" GLOBALS """
# Get & Set Options / Args
parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
parser.add_option("-p", "--path", dest="path", \
                  help="Set project path.", metavar='<PATH>')
(options, args) = parser.parse_args()

PATH = options.path


""" FUNCTIONS """

def exit_program(reason):
    """Terminates program and displays reason why."""
    print reason
    exit()

def display_banner():
    """Prints banner to console."""
    banner = """

       ___________      (     (           *    (          ___________
    ,''..-------..``.   )\ )  )\ )      (  `   )\ )    ,''..-------..``.
    :`-..._____...-':   (()/( (()/(   (  )\))( (()/(   :`-..._____...-':
    |`-..._____...-'|   /(_)) /(_))  )\((_)()\ /(_))   |`-..._____...-'|
    |   |       |   |   (_))_ (_)) _ ((_|_()((_|_))    |   |       |   |
    |]  |       |  [|   |   \| _ \ | | |  \/  | |      |]  |       |  [|
    |   []     []   |   | |) |   / |_| | |\/| | |__    |   []     []   |
    |   |  ___  |   |   |___/|_|_\\\\___/|_|  |_|____|   |   |  ___  |   |
    :`-.:._]|[_.:.-';                                  :`-.:._]|[_.:.-';
     `-...|SSt|...-'           Version 1.00             `-...|SSt|...-'

     """
    print banner


def verify_path():
    """Ensure user specified a valid path."""
    # Did user specify a path? (-p)
    if not PATH:
        reason = "[!] Path not specified! Try running:\n$ python druml.py" \
                 "-p PATH/TO/PROJECTS/\n"
        exit_program(reason)

    # Does user-specified path actually exist?
    elif not os.path.isdir(os.path.expanduser(PATH)):
        reason = "[!] Path does not exist!\nCheck for the correct path on " \
                 "your local machine."
        exit_program(reason)

    # Path specified and exists.
    else:
        print '[*] Path exists, good!'


def main():
    display_banner()
    verify_path()


""" PROCESS """

if __name__ == "__main__":
    main()
