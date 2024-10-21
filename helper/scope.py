class Scope:
    def __init__(self, scope_type, tokens):
        self.scope_type = scope_type
        self.tokens = tokens
        self.nested_scopes = []

    def add_nested_scope(self, nested_scope):
        self.nested_scopes.append(nested_scope)

    def __repr__(self):
        return f"Scope(type=\033[33m{self.scope_type}\033[0m, tokens=\033[34m{self.tokens}\033[0m, nested_scopes={self.nested_scopes})"


def analyzer(matched_braces, tokenized_output):
    root_scope = Scope("root", tokenized_output)
    stack = [(root_scope, float('inf'))]  # Initialize stack with root scope and a high end position

    for key, end_pos in sorted(matched_braces.items(), key=lambda item: int(item[0].split()[1])):
        scope_type, start_pos = key.split()
        start_pos = int(start_pos)
        end_pos = int(end_pos)

        # Extract tokens for the current scope
        scope_tokens = tokenized_output[start_pos:end_pos + 1]
        scope = Scope(scope_type, scope_tokens)

        # Handle nesting
        while stack and stack[-1][1] < start_pos:
            stack.pop()

        stack[-1][0].add_nested_scope(scope)
        stack.append((scope, end_pos))

    return root_scope

# Example usage
matched_braces = {'tuple 0': 3, 'list 7': 8, 'tuple 9': 15, 'tuple 4': 16, 'tuple 17': 19}
tokenized_output = ['(', '(', 'IMPORT', '"example.cell"', ')', '(', 'DEFN', 'main', '[', ']', '(', 'print "Hello', ',', 'world', '!', '"', ')', ')', '(', 'call main', ')', ')']

root_scope = analyzer(matched_braces, tokenized_output)
print(root_scope)