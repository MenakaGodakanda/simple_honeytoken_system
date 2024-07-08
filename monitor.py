import subprocess
import datetime

LOG_FILE = 'logs/honeyfile_log.txt'
HONEYFILE = 'honeyfile.txt'

def log_interaction(event, file):
    with open(LOG_FILE, 'a') as log:
        log.write(f'{datetime.datetime.now()}: {event} {file}\n')

def monitor_honeyfile():
    process = subprocess.Popen(
        ['inotifywait', '-m', '.', '--format', '%e %w%f', '--event', 'open,modify,delete,create'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    for line in process.stdout:
        event, filepath = line.decode('utf-8').strip().split(' ', 1)
        if filepath == f"./{HONEYFILE}":
            log_interaction(event, filepath)

    for line in process.stderr:
        error = line.decode('utf-8').strip()
        log_interaction(f"ERROR: {error}", '')

if __name__ == "__main__":
    monitor_honeyfile()
