import subprocess
import datetime

LOG_FILE = 'logs/honeyfile_log.txt'
HONEYFILE = 'honeyfile.txt'

def log_interaction(event):
    with open(LOG_FILE, 'a') as log:
        log.write(f'{datetime.datetime.now()}: {event}\n')

def monitor_honeyfile():
    process = subprocess.Popen(
        ['inotifywait', '-m', HONEYFILE, '--format', '%e', '--event', 'open,modify,delete'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    for line in process.stdout:
        event = line.decode('utf-8').strip()
        log_interaction(event)

if __name__ == "__main__":
    monitor_honeyfile()
