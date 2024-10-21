def vcel_parser(text, pos):
    if pos < len(text) and text[pos] == "VCEL":
        return ("VCEL", pos + 1)
    return (None, pos)

def defn_parser(text, pos):
    if pos < len(text) and text[pos] == "DEFN":
        return ("DEFN", pos + 1)
    return (None, pos)

def import_parser(text, pos):
    if pos < len(text) and text[pos] == "IMPORT":
        return ("IMPORT", pos + 1)
    return (None, pos)

def int_parser(text, pos):
    if pos < len(text) and text[pos] == "INT":
        return ("INT", pos + 1)
    return (None, pos)

def str_parser(text, pos):
    if pos < len(text) and text[pos] == "STR":
        return ("STR", pos + 1)
    return (None, pos)

def bool_parser(text, pos):
    if pos < len(text) and text[pos] == "BOOL":
        return ("BOOL", pos + 1)
    return (None, pos)

def float_parser(text, pos):
    if pos < len(text) and text[pos] == "FLOAT":
        return ("FLOAT", pos + 1)
    return (None, pos)

def double_parser(text, pos):
    if pos < len(text) and text[pos] == "DOUBLE":
        return ("DOUBLE", pos + 1)
    return (None, pos)

def char_parser(text, pos):
    if pos < len(text) and text[pos] == "CHAR":
        return ("CHAR", pos + 1)
    return (None, pos)

def opening_square_bracket_parser(text, pos):
    if pos < len(text) and text[pos] == "[":
        return ("[", pos + 1)
    return (None, pos)

def closing_square_bracket_parser(text, pos):
    if pos < len(text) and text[pos] == "]":
        return ("]", pos + 1)
    return (None, pos)

def opening_curly_bracket_parser(text, pos):
    if pos < len(text) and text[pos] == "{":
        return ("{", pos + 1)
    return (None, pos)

def closing_curly_bracket_parser(text, pos):
    if pos < len(text) and text[pos] == "}":
        return ("}", pos + 1)
    return (None, pos)

def opening_parenthesis_parser(text, pos):
    if pos < len(text) and text[pos] == "(":
        return ("(", pos + 1)
    return (None, pos)

def closing_parenthesis_parser(text, pos):
    if pos < len(text) and text[pos] == ")":
        return (")", pos + 1)
    return (None, pos)

def semicolon_parser(text, pos):
    if pos < len(text) and text[pos] == ";":
        return (";", pos + 1)
    return (None, pos)

def colon_parser(text, pos):
    if pos < len(text) and text[pos] == ":":
        return (":", pos + 1)
    return (None, pos)

def comma_parser(text, pos):
    if pos < len(text) and text[pos] == ",":
        return (",", pos + 1)
    return (None, pos)

def equal_parser(text, pos):
    if pos < len(text) and text[pos] == "=":
        return ("=", pos + 1)
    return (None, pos)

def plus_parser(text, pos):
    if pos < len(text) and text[pos] == "+":
        return ("+", pos + 1)
    return (None, pos)

def minus_parser(text, pos):
    if pos < len(text) and text[pos] == "-":
        return ("-", pos + 1)
    return (None, pos)

def multiply_parser(text, pos):
    if pos < len(text) and text[pos] == "*":
        return ("*", pos + 1)
    return (None, pos)

def divide_parser(text, pos):
    if pos < len(text) and text[pos] == "/":
        return ("/", pos + 1)
    return (None, pos)

def modulo_parser(text, pos):
    if pos < len(text) and text[pos] == "%":
        return ("%", pos + 1)
    return (None, pos)

def bitwise_and_parser(text, pos):
    if pos < len(text) and text[pos] == "AND":
        return ("AND", pos + 1)
    return (None, pos)

def bitwise_or_parser(text, pos):
    if pos < len(text) and text[pos] == "OR":
        return ("OR", pos + 1)
    return (None, pos)

def bitwise_xor_parser(text, pos):
    if pos < len(text) and text[pos] == "XOR":
        return ("XOR", pos + 1)
    return (None, pos)

def bitwise_not_parser(text, pos):
    if pos < len(text) and text[pos] == "NOT":
        return ("NOT", pos + 1)
    return (None, pos)

