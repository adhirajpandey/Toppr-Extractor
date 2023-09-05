from flask import Flask, render_template, request, Response, jsonify, send_file
import os
from script import url_to_csv
from tasks import url_to_csv_task

app = Flask(__name__)

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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Remove existing files before processing
        remove_existing_files()

        url = request.form.get('url')
        # url_to_csv(url)
        csvtask = url_to_csv_task.delay(url)

        return csvtask.id

    return render_template('index.html')


@app.route('/task/<task_id>', methods=['GET'])
def check_task_status(task_id):
    task = url_to_csv_task.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return jsonify({'status': 'SUCCESS'})
    elif task.state == 'FAILURE':
        return jsonify({'status': 'FAILURE'})
    else:
        return jsonify({'status': 'PENDING'})

@app.route('/download/<task_id>', methods=['GET'])
def download_csv(task_id):
    task = url_to_csv_task.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return send_file(
            CSV_FILENAME,
            mimetype='text/csv',
            as_attachment=True,
            download_name='output.csv'
        )
    else:
        return "CSV generation is still in progress. Please check again later.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
