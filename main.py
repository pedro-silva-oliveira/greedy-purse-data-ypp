'''
This script analyses a ypp chat log, scrapes 
greedy purse data from it and exports it into a
csv file

Sparneejuah and Azariul on Emerald Ocean
'''

import csv
import time
import re

## GLOBAL VARIABLES
# Insert the path to your chat log here:
logPath = r"C:\Users\Pedro\OneDrive\Documentos\Puzzle Pirates\Azariul_emerald_Chat_log"
purse = r"\n\[\d\d:\d\d:\d\d\] Ye slash open the purse to find (\d*) pieces of eight!"
current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

## MAIN CODE
with open(logPath, 'r') as file_in:
    with open(logPath[:-4]+'_purse_data_' + current_time + '.csv', 'w', newline='') as file_out:
        purseresults = re.findall(purse.strip(), file_in.read())
        write = csv.writer(file_out)
        for pursesum in purseresults:
            write.writerow([int(pursesum)])