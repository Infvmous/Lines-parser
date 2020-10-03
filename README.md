# Getting mobile numbers from files on a given line and sorting it or requesting for carrier name of number from file
# Parsing numbers from files
1. Put files with numbers inside to assets folder
2. Set ```parse_line_number = {your_line_number}```
3. Run ```__main__.py``` without arguments to parse
4. As result ```you'll get data-{current_date}({current_time}).json``` file

# Get and sort mobile number by carrier name
1. Put mobile numbers to ```numbers.txt``` without dialing (country) code
2. Run ```__main__.py``` with argument of country code to which the number belongs
3. Numbers and carriers will be saved in ```data``` folder
p.s. better to use https://github.com/Infvmous/Carrier247-parser, it's using the same api but sorting is better
