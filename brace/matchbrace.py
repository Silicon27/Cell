from errors import error

def match_braces(input_string):
    stack = []
    matches = {}

    for i, char in enumerate(input_string):
        if char == '{':
            stack.append(i)
        elif char == '}':
            if stack:
                opening_position = stack.pop()
                matches[f"dict {opening_position}"] = i
            else:
                raise error.UnmatchedBraceError("}", char)

        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                opening_position = stack.pop()
                matches[f"tuple {opening_position}"] = i
            else:
                raise error.UnmatchedBraceError(")", char)

        if char == '[':
            stack.append(i)
        elif char == ']':
            if stack:
                opening_position = stack.pop()
                matches[f"list {opening_position}"] = i
            else:
                raise error.UnmatchedBraceError("]", char)

    if stack:
        for i in stack:
            raise error.UnmatchedBraceError(input_string[i], i)

    return matches
