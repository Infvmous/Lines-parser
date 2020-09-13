import parse
from time import time
import sys


if __name__ == '__main__':
    start_time = time() # Starts timer
    # Check if there arguments entered in terminal
    if len(sys.argv) >= 2:
        arg1 = sys.argv[1]
        # main()
    else:
        # If there is only 1 argument parse operators from multiple files
        parse.main()
    execution_time = (time() - start_time) # Calculate script execution time
    print(f'Run time: {execution_time}s')
    
    
    

