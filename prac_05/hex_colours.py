# Constant dictionary of color names and their hexadecimal codes
COLOR_CODES = {
    "RED": "#ff0000",
    "GREEN": "#00ff00",
    "BLUE": "#0000ff",
    "WHITE": "#ffffff",
    "BLACK": "#000000",
    "YELLOW": "#ffff00",
    "CYAN": "#00ffff",
    "MAGENTA": "#ff00ff",
    "GRAY": "#808080",
    "BROWN": "#a52a2a"
}


def get_color_code(name_of_color):
    """
    Get the hexadecimal code for the given color name.
    Returns None if the color name is not found.
    """
    return COLOR_CODES.get(name_of_color.upper())


while True:
    color_name = input("Enter a color name (or blank to stop): ").strip()
    if not color_name:
        break

    color_code = get_color_code(color_name)
    if color_code:
        print(f"The hexadecimal code for {color_name.capitalize()} is {color_code}.")
    else:
        print("Invalid color name. Please try again.")
