def wich_delimiter(string):
    string = str(string)
    space = string.count(' ')
    rest = string.count(',')
    tab = string.count('\t')
    if space == 0 and rest == 0 and tab == 0:
        return "AssertionError"
    else:
        max_ = max(space, rest, tab)
        if max_ == space:
            return 'space'
        elif max_ == rest:
            return "rest"
        else:
            return "tab"