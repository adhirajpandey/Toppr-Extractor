#!/bin/bash

source venv/bin/activate

# Check if the Flask server process is running
if ps aux | grep -v grep | grep "python3 app.py" >/dev/null; then
    # Flask server process is running, capture its PID
    pid=$(ps aux | grep -v grep | grep "python3 app.py" | awk '{print $2}')

    echo "PID is: $pid"

    # Kill the Flask server process
    sudo kill -9 $pid

    echo "Process killed successfully."
else
    echo "No process found."
fi

nohup python3 app.py >> flasknohup.out 2>&1 &

nohup celery -A tasks worker -l info >> celerynohup.out 2>&1 &


echo "New Flask Server and Celery Worker started successfully."
