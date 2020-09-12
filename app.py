from datetime import datetime
import json
from glob import glob
import re
from time import time


def create_or_update_value(dictionary, key):
    # If key exists -> increase value of it by 1
    # If doesn't -> set value to 1
    if key in dictionary.keys():
        dictionary[key][0] += 1
    else:
        dictionary.setdefault(key, [])
        dictionary[key].append(1)


def write_json(dictionary, date):
    # Dump dict to json then write to json file
    with open(f'data-{date}.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent = 4)


def parse(dictionary, folder_name, line_number):
    # Opening all files from the directory
    # Look for one line in opened file
    # Collect formatted strings from files in dictionary as key:value
    count = 0 
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
                count += 1
                print(f'{name}: {dictionary[name]}')
        myfile.close()
    return dictionary, count


def calculate_percentage(dictionary, total):
    for key in dictionary:
        percentage = f'{round(dictionary[key][0] / total * 100, 2)}%'
        dictionary[key].append(percentage)
    return dictionary


def main():
    # Config variables
    folder_name = 'assets'
    parse_line_number = 29
    dictionary = {}

    # Main script
    current_datetime = datetime.now().strftime("%m-%d-%y(%H-%M-%S)")
    parsed_dictionary = parse(dictionary, folder_name, parse_line_number)
    operators_dict = calculate_percentage(parsed_dictionary[0], parsed_dictionary[1])
    sorted_dict = sorted(operators_dict.items(), key=lambda x: x[1], reverse=True)

    write_json(sorted_dict, current_datetime)


if __name__ == '__main__':
    start_time = time() # Starts timer
    main()
    execution_time = (time() - start_time) # Calculate script execution time
    print(f'Run time: {execution_time}s')

