def xprint(text, color="white", background="", options=""):
    """
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
    
    Credits:
        https://github.com/Haj4li
    """

    color_mapping = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "light_gray": "90",
        "light_red": "91",
        "light_green": "92",
        "light_yellow": "93",
        "light_blue": "94",
        "light_magenta": "95",
        "light_cyan": "96",
        "light_white": "97",
    }

    background_mapping = {
        "black": "40",
        "red": "41",
        "green": "42",
        "yellow": "43",
        "blue": "44",
        "magenta": "45",
        "cyan": "46",
        "white": "47",
    }

    option_mapping = {
        "bold": "1",
        "underline": "4",
        "reverse": "7",
    }

    color_code = color_mapping.get(color.lower(), "37")
    background_code = background_mapping.get(background.lower(), "")
    option_codes = [option_mapping.get(opt.lower(), "0") for opt in (options or "").split()]

    if background_code:
        color_background_code = f"{color_code};{background_code}"
    else:
        color_background_code = color_code

    full_code = ";".join([color_background_code] + option_codes)

    start_code = f"\033[{full_code}m"
    end_code = "\033[0m"

    print(f"{start_code}{text}{end_code}")
