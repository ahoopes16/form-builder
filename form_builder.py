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
OUTPUT_FILE = "mynewform.html"

#############
# FUNCTIONS #
#############

def handle_error_and_exit(custom_message, error):
    """Prints out the error, along with a custom message and exits."""

    print(custom_message)
    print("Received the error: {}".format(error))
    exit(1)

def get_input_from_file():
    """Get the user input from the forms.txt file.
    @return form_components: the components from the file
    """

    try:
        with open(INPUT_FILE) as inputs:
            form_components = inputs.readlines()

        form_components = [comp.strip() for comp in form_components]

    except Exception as error:
        custom_message = "Could not open the file {}.\n".format(INPUT_FILE)
        custom_message += "Please check to make sure the file is in this " +\
                          "directory and is named 'forms.txt'."
        handle_error_and_exit(custom_message, error)

    return form_components

def get_input_from_cmd_line():
    """Parse the user input from the command line arguments.
    @return sys.argv[1:]: the components from the command line args
    """

    # The first arg is always the name of the script, cut that off
    return sys.argv[1:]

def get_input():
    """Get the user input, either from cmd line or a .txt file
    @return form_components: the form components from input
    """

    # No command line arguments were given, use text file
    if len(sys.argv) == 1:
        form_components = get_input_from_file()

    # Command line arguments were given, use them
    else:
        form_components = get_input_from_cmd_line()

    return form_components

def build_html_file_head():
    """Build the beginning of the HTML file.
    @return html_contents: The contents of the HTML file head
    """

    html_contents = "<!DOCTYPE html>\n"
    html_contents += "<html>\n"
    html_contents += "    <head>\n"
    html_contents += "        <title>My Automated Form</title>\n"
    html_contents += "        <meta charset='UTF-8'>\n"
    html_contents += "    </head>\n"
    html_contents += "    <body>\n"
    html_contents += "        <h2>Your Form</h2>\n"
    html_contents += "        <form>\n"

    return html_contents



def build_html_file_foot():
    """Build the ending of the HTML file.
    @return html_contents: The contents of the HTML file foot
    """

    html_contents = '<input type="submit" value="Submit">'
    html_contents += "        </form>\n"
    html_contents += "    </body>\n"
    html_contents += "</html>"

    return html_contents

def export_html_file(html):
    """Export the HTML contents to an output file.
    @param html: The HTML contents to write to the file
    """

    try:
        output_file = open(OUTPUT_FILE, 'w+')
        output_file.write(html)
        output_file.close()
    except Exception as error:
        custom_message = "Could not open file {}\n".format(OUTPUT_FILE)
        custom_message += "Please make sure that I have permission " + \
                          "to create/edit files in this directory."
        handle_error_and_exit(custom_message, error)

def main():
    """The main function that runs the script."""

    # Get input
    form_components = get_input()

    # Build HTML leading up to the form
    html = build_html_file_head()

    # Build individual form components based on input
    html += build_html_form_elements()

    # Build HTML to close out the form
    html += build_html_file_foot()

    # Export to .html file
    export_html_file(html)

main()
