from playwright.sync_api import Playwright, sync_playwright
from undetected_playwright import stealth_sync
import time
from bs4 import BeautifulSoup
import json

def convert_to_api_url(input_url):
    if "toppr.com/ask/question-set" in input_url:
        parts = input_url.split("/")
        question_set_id = parts[-3].split("-")[-1]
        level = parts[-2]
        api_url = f"https://www.toppr.com/api/v1/open/question-set/{question_set_id}/{level}/?page="
        return api_url
    else:
        return None

def run(playwright: Playwright, input_url) -> int:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    stealth_sync(context)
    
    page = context.new_page()

    final_url = convert_to_api_url(input_url + '1')

    # print(final_url)

    page.goto(final_url)

    time.sleep(0.5)

    #capture html response
    html_response = page.content()

    #parse html response using beautifulsoup to filter only json data
    soup = BeautifulSoup(html_response, 'html.parser')
    pre_element = soup.find('pre')
    json_string = pre_element.string.strip()

    #convert json string to python dictionary
    data_dict = json.loads(json_string)

    # print(type(data_dict))

    total_pages = data_dict['page_info']['total_pages']

    api_call_url = convert_to_api_url(input_url)

    # print(total_pages)

    context.close()
    browser.close()

    return api_call_url,total_pages




#need to get variable of total pages in first request
def get_total_pages(input_url):
    with sync_playwright() as playwright:
        total_pages = run(playwright, input_url)
    return total_pages

# if __name__ == '__main__':
#     print("Total Pages :",get_total_pages('https://www.toppr.com/ask/question-set/hydrocarbons-432904/medium/'))