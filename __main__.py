import parse
import request
from time import time
import sys
from dotenv import load_dotenv
import json
from datetime import datetime


def write_json(dictionary, date, filename = 'data'):
    # Dump dict to json then write to json file
    with open(f'data/{filename}-{date}.json', 'w') as outfile:
        json.dump(dictionary, outfile, indent = 4)


if __name__ == '__main__':
    start_time = time() # Starts timer
    current_datetime = datetime.now().strftime("%m-%d-%y(%H-%M-%S)") 
    # Check if there arguments entered in terminal
    if len(sys.argv) >= 2:
        filename = 'response'
        load_dotenv()
        data = request.main(sys.argv[1])
        write_json(data, current_datetime, filename)
    else:
        # If there is only 1 argument parse operators from multiple files
        data = parse.main()
        write_json(data, current_datetime)
    execution_time = (time() - start_time) # Calculate script execution time
    print(f'Run time: {execution_time}s')
    
    
    

