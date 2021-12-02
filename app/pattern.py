


## --------------------------------------------------------------------- ##

# Check pattern of hostname and create group base on it
def pattern_reader(file):
    pattern_list = []
    with open(file, 'r') as pattern_file:
        for pattern in pattern_file.readlines():
            if str(pattern)[-1] == '\n':
                pattern_list.append(pattern[:-1])
            elif str(pattern)[-1] != '\n' and len(str(pattern)) >= 3:
                pattern_list.append(pattern)
    return pattern_list