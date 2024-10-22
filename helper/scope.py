def analyzer(tokenized_output, matched, w_spaces):
    # remove the type of the matched braces and have a dict of starting and ending indexes from matched:
    matched2 = {}
    root_values = []
    scopes = []
    scopes_w_spaces = []


    #
    for key, value in matched.items():
        if key.startswith("list"):
            continue
        matched2[int(key.split()[1])] = value
    
    # sort it based on the largest value
    matched2 = dict(sorted(matched2.items(), key=lambda item: item[1], reverse=True))

    # print(matched2)
    
    for key, value in matched2.items():
        i = tokenized_output[key+1:value]
        i_w_spaces = w_spaces[key+1:value]
        if key == 0:
            continue
        # print(i)
        scopes.append(i)
        scopes_w_spaces.append(i_w_spaces)
        try: 
            if i[0] == "ROOT":
                root_values.append(i)
        except IndexError:
            pass
    return scopes, root_values, scopes_w_spaces

def visualizer(scopes: list[list]):
    # Invert all items in the list

    scopes.reverse()

    for i in scopes:
        print(i)
    


# # Example usage
# matched_braces = {'tuple 1': 4, 'list 8': 9, 'tuple 10': 16, 'tuple 5': 17, 'tuple 18': 20, 'tuple 0': 21}
# tokenized_output = ['(', '(', 'IMPORT', '"example.cell"', ')', 
#                     '(', 'DEFN', 'main', '[', ']', '(', 'print "Hello', ',', 'world', '!', '"', ')', ')', '(', 'call main', ')', ')']

# analyzer(tokenized_output, matched_braces)