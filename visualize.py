import matplotlib.pyplot as plt
import datetime

LOG_FILE = 'logs/honeyfile_log.txt'

def read_log():
    events = []
    with open(LOG_FILE, 'r') as log:
        for line in log:
            timestamp, event = line.split(': ', 1)
            timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
            events.append((timestamp, event.strip()))
    return events

def plot_events(events):
    timestamps = [event[0] for event in events]
    event_types = [event[1] for event in events]

    plt.figure(figsize=(10, 5))
    plt.hist(timestamps, bins=30, edgecolor='black')
    plt.xlabel('Time')
    plt.ylabel('Number of Interactions')
    plt.title('Honeyfile Interactions Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/honeyfile_interactions.png')
    plt.show()

if __name__ == "__main__":
    events = read_log()
    plot_events(events)
