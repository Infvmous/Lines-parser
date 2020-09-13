from datetime import datetime
import json
from glob import glob
import re


def fill_dictionary(dictionary, key, phone_number = None):
    # If key exists -> increase value of it by 1
    # If doesn't -> set value to 1
    total_numbers_key = 'Total_numbers'
    numbers_key = 'Numbers'
    if key in dictionary:
        dictionary[key][total_numbers_key][0] += 1
    else:
        dictionary.setdefault(key, {})
        dictionary[key][total_numbers_key] = [1]
    # Collect numbers for specific operator
    if phone_number:
        if numbers_key in dictionary[key]:
            dictionary[key][numbers_key].append(phone_number)
        else:
            dictionary[key].setdefault(numbers_key, [])
            dictionary[key][numbers_key].append(phone_number)
    
    
def calculate_percentage(dictionary, total):
    for key in dictionary:
        key2 = 'Total_numbers'
        percentage = f'{round(dictionary[key][key2][0] / total * 100, 2)}%'
        dictionary[key][key2].append(percentage)
    return dictionary


def write_json(dictionary, date):
    # Dump dict to json then write to json file
    with open(f'data/data-{date}.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent = 4)


def parse(data_dict, folder_name, line_number, starts_with_0 = True):
    # Opening all files from the directory
    # Look for one line in opened file
    # Collect formatted strings from files in dictionary as key:value
    count = 0 
    for file in glob(f'{folder_name}/*'):
        myfile = open(file, 'r')
        for index, line in enumerate(myfile):
            if index == line_number:
                
                # Collect phone numbers from filename
                # phone_number = re.search(r"assets\\((07).\d{8})_", file)
                # if phone_number is not None:
                #     result = phone_number.group(1)
                #     print(result)
                # else:
                #     print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')


                operator_obj = re.search(r"'(.*?)'", line)
                number_obj = re.search(r"assets\\((07).\d{8})_", file)

                if operator_obj is not None:
                    if number_obj is not None:
                        number = number_obj.group(1)
                    else:
                        number = None
                    operator = operator_obj.group().replace("'", '')
                    fill_dictionary(data_dict, operator, number)
                else:
                    fill_dictionary(data_dict, 'other')
                count += 1
                # print(f'{name}: {data_dict[name]}')
        myfile.close()
    return data_dict, count


def main():
    # Config variables
    assets_folder_name = 'assets'
    parse_line_number = 29
    data = {}

    # Main script
    current_datetime = datetime.now().strftime("%m-%d-%y(%H-%M-%S)")
    parsed_dictionary = parse(data, assets_folder_name, parse_line_number)
    operators_dict = calculate_percentage(parsed_dictionary[0], parsed_dictionary[1])

    write_json(operators_dict, current_datetime)