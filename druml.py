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

OUTPUT_DIR = "DIAGRAMS"

projects_in_path = []


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


def install_phuml():
    """Git clones the phUML repo; it's a required dependency."""
    PHUML_URL = "https://github.com/jakobwesthoff/phuml.git"
    rc = subprocess.call(['git', 'clone', PHUML_URL])
    print '[*] Installed: phUML'


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


def verify_installed_dependencies():
    """Ensure user has downloaded and installed necessary dependencies."""

    print '[*] Checking dependencies exist...'

    # Has phUML been downloaded?
    if not os.path.isdir('phuml'):

        print '[!] Not Found: phUML'

        # Prompt user to download missing phUML.
        choice = raw_input('Install phUML (y|n)? ')
        if choice.lower() =='y' or choice.lower() == 'yes':
            install_phuml()
        else:
            reason = "[!] phuml is required to run this program."
            exit_program(reason)
    else:
        print '[*] Found: phUML, good!'

    print '[*] No missing dependencies, good!'


def read_projects_in_path():
    """Fill global list with names of projects in specified path."""
    global projects_in_path
    projects_in_path = os.walk(PATH).next()[1]


def verify_projects():
    """Verify that the specified path actually has projects in it."""
    if projects_in_path:
        print '[*] Projects exist in specified path, good!'
    else:
        reason = '[!] No projects exist in specified directory.'
        exit_program(reason)


def create_diagram_dir():
    """Create directory to store generated Class Diagrams."""
    # If OUTPUT_DIR hasn't been made yet, make it.
    if not os.path.isdir(OUTPUT_DIR):
        rc = subprocess.call(['mkdir', OUTPUT_DIR])
        print '[!] Creating Directory: %s' % OUTPUT_DIR
    else:
        print '[*] Directory %s already exists, good!' % OUTPUT_DIR


def generate_diagrams():
    PATH_TO_PHUML = 'phuml/src/app/'
    for module in projects_in_path:
        MODULE_NAME = module
        PATH_TO_MODULE = '%s/%s' % (PATH, MODULE_NAME)
        rc = subprocess.call(['./phuml', '-r', PATH_TO_MODULE, '-graphviz', '-createAssociations', 'false', '-neato', '%s.png' % MODULE_NAME], cwd=PATH_TO_PHUML)
        rc = subprocess.call(['mv', '%s.png' % MODULE_NAME, '../../../%s' % OUTPUT_DIR], cwd=PATH_TO_PHUML)


def main():
    display_banner()
    verify_path()
    verify_installed_dependencies()
    read_projects_in_path()
    verify_projects()
    create_diagram_dir()
    generate_diagrams()



""" PROCESS """

if __name__ == "__main__":
    main()
