class colored_string:
    ESCAPE_CODE = '\033['
    GREEN_TEXT = '32m'
    BRIGHT_GREEN_TEXT = '92m'
    RED_TEXT = '31m'
    YELLOW_TEXT = '93m'
    EOC = '\033[0m'

def yellow(str):
    return colored_string.ESCAPE_CODE + colored_string.YELLOW_TEXT + str + colored_string.EOC

def green(str):
    return colored_string.ESCAPE_CODE + colored_string.GREEN_TEXT + str + colored_string.EOC

def red(str):
    return colored_string.ESCAPE_CODE + colored_string.RED_TEXT + str + colored_string.EOC

def bright_green(str):
    return colored_string.ESCAPE_CODE + colored_string.BRIGHT_GREEN_TEXT + str + colored_string.EOC
