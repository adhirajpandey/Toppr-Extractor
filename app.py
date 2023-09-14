from flask import Flask, render_template, request, Response, jsonify, send_file
from tasks import toppr_task

DATA_DIR = 'DATA'
CSV_FILENAME = 'out.csv'

def valid_url(url):
    if "toppr" in url and "question-set" in url:
        return True
    else:
        return False
    

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        print("Input Link : ", url)
        if valid_url(url):
            if url[-1] == '/':
                csvtask = toppr_task.delay(url)
            else:
                csvtask = toppr_task.delay(url + '/')
            
            return csvtask.id
        else:
            return "Invalid URL", 400

    return render_template('index.html')


@app.route('/task/<task_id>', methods=['GET'])
def check_task_status(task_id):
    task = toppr_task.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return jsonify({'status': 'SUCCESS'})
    elif task.state == 'FAILURE':
        return jsonify({'status': 'FAILURE'})
    else:
        return jsonify({'status': 'PENDING'})
    

@app.route('/download/<task_id>', methods=['GET'])
def download_csv(task_id):
    task = toppr_task.AsyncResult(task_id)
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
    app.run(host='0.0.0.0', port=4322)
