from playwright.sync_api import Playwright, sync_playwright
from undetected_playwright import stealth_sync
import time
from bs4 import BeautifulSoup


data_dir = 'DATA/'

def run(playwright: Playwright, api_url, total_pages) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    stealth_sync(context)
    
    page = context.new_page()

    # total_pages = 5
    
    for i in range(1, total_pages + 1):
        try:
            # page.goto(f"https://www.toppr.com/api/v1/open/question-set/432904/medium/?page={i}")
            page.goto(f"{api_url}{i}")
        
            time.sleep(1)

            #capture html response
            html_response = page.content()

            #parse html response using beautifulsoup to filter only json data
            soup = BeautifulSoup(html_response, 'html.parser')
            pre_element = soup.find('pre')
            json_data = pre_element.string.strip()

            
            #save json response
            with open(f'{data_dir}data{i}.json', 'w') as f:
                f.write(json_data)

            print(f"Page {i} Fethced and Saved")
        except Exception as e:
            pass

    context.close()
    browser.close()


def fetch_data(api_call_url, total_pages):
    with sync_playwright() as playwright:
        run(playwright, api_call_url, total_pages)
    return None

# if __name__ == "__main__":
#     api_call_url = 'https://www.toppr.com/api/v1/open/question-set/432904/medium/?page='
#     total_pages = 5
#     with sync_playwright() as playwright:
#         run(playwright, api_call_url, total_pages)



#need to get variable of total pages in first request