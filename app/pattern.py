from os.path import exists
import yaml

## --------------------------------------------------------------------- ##

# Check pattern of hostname and create group base on it
def pattern_reader(ymlFile):
    pattern_list = []
    if exists(ymlFile):
        with open(ymlFile, 'r') as pattern_file:
            pattern_file_buffer = yaml.load(pattern_file, Loader=yaml.FullLoader)
            for pattern_title, patterns in pattern_file_buffer.items():
                for pattern in patterns:
                    pattern_list.append(pattern)
    else:
        sample_pattern = [{'patterns': ['([sS]ervers?)']}]
        with open(ymlFile, 'w') as pattern_file:
            pattern = '([sS]ervers?)'
            yaml.dump(sample_pattern, pattern_file)
            pattern_list.append(sample_pattern['patterns'][0])
    return pattern_list