from datetime import datetime
import json
from glob import glob
import re
from time import time


def create_or_update_value(dictionary, key):
    # If key exists -> increase value of it by 1
    # If doesn't -> set value to 1
    if key in dictionary.keys():
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def write_json(dictionary, date):
    # Dump dict to json then write to json file
    with open(f'data-{date}.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent = 4)


def parse(dictionary, folder_name, line_number):
    # Opening all files from the directory
    # Look for one line in opened file
    # Collect formatted strings from files in dictionary as key:value 
    for file in glob(f'{folder_name}/*'):
        myfile = open(file, 'r')
        for index, line in enumerate(myfile):
            if index == line_number:
                re_obj = re.search(r"'(.*?)'", line)
                if re_obj is not None:
                    name = re_obj.group().replace("'", '')
                    create_or_update_value(dictionary, name)
                else:
                    create_or_update_value(dictionary, 'other')
                print(f'{name}: {dictionary[name]}')
        myfile.close()
    return dictionary


def main():
    # Config variables
    folder_name = 'assets'
    parse_line_number = 29
    dictionary = {}
    
    # Main script
    current_datetime = datetime.now().strftime("%m-%d-%y(%H-%M-%S)")
    operators_dict = parse(dictionary, folder_name, parse_line_number)
    write_json(operators_dict, current_datetime)


if __name__ == '__main__':
    start_time = time() # Starts timer
    main()
    execution_time = (time() - start_time) # Calculate script execution time
    print(execution_time)

