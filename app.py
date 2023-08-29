from flask import Flask, render_template, request, Response
import os
from script import url_to_csv

app = Flask(__name__)

DATA_DIR = 'DATA'
CSV_FILENAME = 'out.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Remove existing files before processing
        remove_existing_files()

        url = request.form.get('url')
        url_to_csv(url)

        return Response(
            open(CSV_FILENAME, 'rb'),
            mimetype='text/csv',
            headers={'Content-Disposition': f'attachment; filename={CSV_FILENAME}'}
        )

    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
