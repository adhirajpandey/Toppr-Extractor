from total import get_total_pages
from extract import fetch_data
from merge import merge_json_files
from makecsv import create_csv
import os

def url_to_csv(input_url):
    api_call_url, total_pages = get_total_pages(input_url)
    fetch_data(api_call_url, total_pages)

    print("Total Pages: ", total_pages)

    #create required directories if not present
    if not os.path.exists('DATA'):
        os.makedirs('DATA')

    merge_json_files('DATA/', 'DATA/merged_data.json')

    create_csv('DATA/merged_data.json', 'out.csv')

    print("Successfully created csv file out.csv")


# input_url = 'https://www.toppr.com/ask/question-set/hydrocarbons-432904/medium/'

# api_call_url, total_pages = get_total_pages(input_url)

# # print("Total Pages :", total_pages)

# total_pages = 10
# #storing all page responses in DATA folder
# fetch_data(api_call_url, total_pages)

# merge_json_files('DATA/', 'Final/merged_data.json')

# create_csv('Final/merged_data.json', 'Final/out.csv')

# print("Successfully created csv file Final/out.csv")