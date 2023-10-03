#!/bin/bash

sleep 10

# Change working directory to /home/ubuntu/Deepgaze-API/
cd '/home/adhiraj/Desktop/Projects/Toppr Celery'

source venv/bin/activate

# Check if the Flask server process is running
if ps aux | grep -v grep | grep "python3 app.py" >/dev/null; then
    # Flask server process is running, capture its PID
    pid1=$(ps aux | grep -v grep | grep "python3 app.py" | awk '{print $2}')

    echo "PID1 is: $pid1"

    # Kill the Flask server process
    sudo kill -9 $pid1

    echo "Flask Process killed successfully."

    pid2=$(ps aux | grep -v grep | grep "celery -A tasks worker -l info" | awk '{print $2}')

    echo "PID2 is: $pid2"

    # Kill the Celery process
    sudo kill -9 $pid2

    echo "Celery Process killed successfully."

    pid3=$(ps aux | grep -v grep | grep "1280x1024x24" | awk '{print $2}')

    echo "PID3 is: $pid3"

    # Kill the xvfb process
    sudo kill -9 $pid3

    echo "xvfb display Process killed successfully."

else
    echo "No process found."
fi

# Start the Flask server again but with virtual display
nohup python3 app.py >> flasknohup.out 2>&1 &
# xvfb-run -a -s "-screen 0 1280x1024x24" nohup python3 app.py >> nohup.out 2>&1 &

xvfb-run -a -s "-screen 0 1280x1024x24" nohup celery -A tasks worker -l info >> celerynohup.out 2>&1 &


echo "New Flask Server and Celery Worker started successfully."
