"""This script will take in a series of labels and the type of
input they should be. It will generate a valid HTML file of
the form in question.
@author: Kevin Hoopes
@version: July 29, 2018
"""

###########
# IMPORTS #
###########

from pprint import pprint
import sys

#############
# CONSTANTS #
#############

INPUT_TYPES = ["text", "date"]
INPUT_FILE = "forms.txt"

#############
# FUNCTIONS #
#############

def get_input_from_file():
    """Get the user input from the forms.txt file.
    @return form_components the components from the file
    """

    with open(INPUT_FILE) as inputs:
        form_components = inputs.readlines()

    form_components = [comp.strip() for comp in form_components]
    return form_components

def get_input_from_cmd_line():
    """Parse the user input from the command line arguments.
    @return form_components the components from the command line args
    """

    # The first arg is always the name of the script, cut that off
    form_components = sys.argv[1:]

    return form_components

def get_input():
    """Get the user input, either from cmd line or a .txt file"""

    # No command line arguments were given, use text file
    if len(sys.argv) == 1:
        form_components = get_input_from_file()

    # Command line arguments were given, use them
    else:
        form_components = get_input_from_cmd_line()

    return form_components

def main():
    """The main function that runs the script."""

    # Get input
    form_components = get_input()
    print("These are the form components:")
    pprint(form_components)

    # Build HTML leading up to the form

    # Build individual form components based on input

    # Build HTML to close out the form

    # Export to .html file

    print("We're going to build a form in HTML!")

main()
