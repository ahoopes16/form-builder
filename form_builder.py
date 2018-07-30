"""This script will take in a series of labels and the type of
input they should be. It will generate a valid HTML file of
the form in question.
@author: Kevin Hoopes
@version: July 29, 2018
"""

###########
# IMPORTS #
###########

import json
from pprint import pprint

#############
# CONSTANTS #
#############

INPUT_TYPES = ["text", "date"]
INPUT_FILE = "elements.json"
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
    @return form_elements: the components from the file
    """

    try:
        elements = open(INPUT_FILE, 'r')
        form_elements = json.load(elements)

    except IOError as error:
        custom_message = "Could not open the file {}.\n".format(INPUT_FILE)
        custom_message += "Please check to make sure the file is in this " +\
                          "directory and is named 'forms.txt'."
        handle_error_and_exit(custom_message, error)

    return form_elements

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

def build_html_form_elements(elements):
    """Build the HTML for each of the form elements.
    @param elements: The form elements to convert to HTML.
    @return html_contents: The HTML generated for the elements
    """
    return ""

def build_html_file_foot():
    """Build the ending of the HTML file.
    @return html_contents: The contents of the HTML file foot
    """

    html_contents = '            <input type="submit" value="Submit">\n'
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
    except IOError as error:
        custom_message = "Could not open file {}\n".format(OUTPUT_FILE)
        custom_message += "Please make sure that I have permission " + \
                          "to create/edit files in this directory."
        handle_error_and_exit(custom_message, error)

def main():
    """The main function that runs the script."""

    # Get input
    form_elements = get_input_from_file()

    # Build HTML leading up to the form
    html = build_html_file_head()

    # Build individual form components based on input
    html += build_html_form_elements(form_elements)

    # Build HTML to close out the form
    html += build_html_file_foot()

    # Export to .html file
    export_html_file(html)

main()
