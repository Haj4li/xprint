# xprint

A Print module for python to print colored text on terminal
This module uses ANSI escape codes to achieve colored text and styling so only works on Linux OS

Print colored text on console or terminal.

    Args:
        text (str): The text to be printed.
        color (str, optional): The text color. Default is "white".
        background (str, optional): The background color. Default is None (no background color).
        options (str, optional): Additional options for styling. Default is None.

    Supported Colors (case-insensitive):
    - black
    - red
    - green
    - yellow
    - blue
    - magenta
    - cyan
    - white
    - light_gray
    - light_red
    - light_green
    - light_yellow
    - light_blue
    - light_magenta
    - light_cyan
    - light_white

    Supported Options:
    - bold
    - underline
    - reverse

    Example:
        xprint("Hello, colored world!", color="green", background="yellow", options="bold")

Just import the module and use it
Check main.py file for examples
