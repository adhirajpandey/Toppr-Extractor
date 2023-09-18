# Toppr-Extractor

## Description
This Python tool allows you to efficiently convert links of Toppr questions into a single CSV file with solutions as well as meta-data. It leverages Playwright for web automation, Beautiful Soup for HTML parsing, and Celery for background task processing, along with HTML, CSS, JS and Flask for creating a simple web interface.

## Installation and Usage
1. Clone the project to your local system using: `git clone https://github.com/adhirajpandey/Toppr-Extractor`

2. Create a virtual environment and activate it: `python -m venv venv && source venv/bin/activate`

3. Install the required dependencies: `pip install -r requirements.txt`

4. If you are using playwright for first time, you would also need to install its browser dependencies: `playwright install`

5. Create empty DATA directory, Run Flask App and Celery Worker using `bash start.sh`

6. Open your web browser and navigate to `http://localhost:4322`.

7. Paste the Toppr question link in the provided input field.

8. Click the "Generate CSV" button, and the tool will gather information from the provided links and generate a CSV file.

9. "Download CSV" button will appear once celery worker has completed the task, click it to download the CSV file.

## Working
![Arch](https://github.com/adhirajpandey/Toppr-Extractor/assets/87516052/ad17513f-823e-408c-b967-b929d8fa6e88)


## Limitations
1. This tool relies on web automation and HTML parsing, which might break if the structure of Toppr's website changes significantly.
2. The accuracy and effectiveness of the tool are dependent on the stability of the Playwright, Beautiful Soup, and Flask libraries, as well as the underlying operating system.

## Disclaimer
This project is not affiliated with Toppr or its services. It's an independent tool created for educational and personal use.

