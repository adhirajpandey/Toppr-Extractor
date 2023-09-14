from celery import Celery
from script import url_to_csv
import os


DATA_DIR = 'DATA'
CSV_FILENAME = 'out.csv'


def remove_existing_files():
    # Remove all files in the DATA directory
    for filename in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    # Remove the out.csv file if it exists
    if os.path.exists(CSV_FILENAME):
        try:
            os.remove(CSV_FILENAME)
        except Exception as e:
            print(f"Error deleting {CSV_FILENAME}: {e}")


app = Celery('tasks', backend='db+sqlite:///db.sqlite', broker='sqla+sqlite:///db.sqlite')


@app.task
def toppr_task(input_url):
    remove_existing_files()
    url_to_csv(input_url)
    
    return 'Done'

