class UnmatchedBraceError(Exception):
    def __init__(self, brace, position):
        self.brace = brace
        self.position = position

    def __str__(self):
        if self.brace == "(":
            return f"Unmatched opening parenthesis at position {self.position}. Expected ')'."
        elif self.brace == "[":
            return f"Unmatched opening square bracket at position {self.position}. Expected ']'."
        elif self.brace == "{":
            return f"Unmatched opening curly brace at position {self.position}. Expected '}}'."
        elif self.brace == ")":
            return f"Unmatched closing parenthesis at position {self.position}. Expected '('."
        elif self.brace == "]":
            return f"Unmatched closing square bracket at position {self.position}. Expected '['."
        elif self.brace == "}":
            return f"Unmatched closing curly brace at position {self.position}. Expected '{{'."
        return f"Unmatched brace '{self.brace}' at position {self.position}"