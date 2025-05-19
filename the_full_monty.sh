#!/bin/bash

# Step 1: Run the RTSP capture and processing script
echo "[`date`] Starting RTSP processing..." >> /home/thor/upload_log.txt
bash /home/thor/RTSP-2-YouTube-short-scaled2.sh

# Check if the RTSP script completed successfully
if [ $? -ne 0 ]; then
    echo "[`date`] RTSP script failed. Aborting upload." >> /home/thor/upload_log.txt
    exit 1
fi

# Step 2: Activate Python virtual environment
echo "[`date`] RTSP complete. Starting upload..." >> /home/thor/upload_log.txt
source /home/thor/gapi-env/bin/activate

# Step 3: Run the YouTube upload Python script
python /home/thor/youtube_upload_dated_ai.py

# Optional: deactivate environment
deactivate
