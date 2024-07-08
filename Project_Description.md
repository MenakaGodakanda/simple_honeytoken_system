# Simple Honeytoken System - Version 1

The Simple Honeytoken System is a security project designed to create a decoy file (honeyfile), monitor interactions with it, log those interactions, and visualize the log data. This project aims to detect unauthorized access or suspicious activities by using open-source tools.

## Features

- **Honeyfile Creation**: A decoy file (`honeyfile.txt`) with fake sensitive information.
- **File Monitoring**: Continuous monitoring of the honeyfile for any interactions using `inotifywait`.
- **Logging**: Records interactions in a log file.
- **Visualization**: Generates a visual representation of interactions over time.
- **Web Interface**: Displays the log and the visualization through a simple Flask web application.

## Coding

### Monitors the Honeyfile and Logs Interactions (`monitor.py`)
This script monitors interactions with the honeyfile (`honeyfile.txt`) using `inotifywait` and logs these interactions.

#### Explanation:
- `import subprocess` and `import datetime`: Importing required modules.
- `LOG_FILE` and `HONEYFILE`: Defining the log file path and honeyfile path.
- `log_interaction(event, file)`: A function to append interaction events to the log file with a timestamp.
- `monitor_honeyfile()`:
    - `subprocess.Popen`: Runs the `inotifywait` command to monitor the honeyfile.
    - `-m`: Stands for monitor mode, allowing continuous monitoring.
    - `--format '%e %w%f'`: Formats the output to show the event type and the file path.
    - `--event 'open,modify,delete,create'`: Specifies the events to monitor.
    - `For loop`: Reads and logs each event from the subprocess output.
- The `if __name__ == "__main__":` block ensures that the monitor_honeyfile function is called only if the script is run as the main module.

### Reads the Log and Generates a Visualization Plot (`visualize.py`)
This script reads the log file and generates a visualization of the interactions using `matplotlib`.

#### Explanation:
- `import matplotlib.pyplot as plt` and `import datetime`: Importing required modules.
- `LOG_FILE`: Defines the log file path.
- `read_log()`:
    - Reads the log file line by line.
    - Parses each line to extract the timestamp and event type.
    - Converts the timestamp to a `datetime` object.
    - Appends the parsed data to the `events` list.
- `plot_events(events)`:
    - Extracts timestamps and event types from the `events` list.
    - Creates a histogram of interaction timestamps.
    - Customizes the plot with labels, title, and formatting.
    - Saves the plot as an image in the `static` directory and displays it.
- The `if __name__ == "__main__":` block reads the log and generates the plot when the script is executed.

### Sets Up a Flask Web Server to Display the Log and the Plot (`app.py`)
This script sets up a Flask web server to display the log content and the visualization plot.

#### Explanation:

- `from flask import Flask, render_template, send_from_directory`: Importing required modules from Flask.
- `app = Flask(__name__)`: Initializing the Flask app.
- `@app.route('/')`: Defines the route for the home page.
  - `index()`:
    - Reads the log file and stores its content in a list.
    - Passes the log content to the `index.html` template for rendering.
- `@app.route('/static/<path:filename>')`: Defines the route for serving static files.
  - `static_files(filename)`:
    - Returns the requested file from the `static` directory.
- The `if __name__ == "__main__":` block runs the Flask app in debug mode when the script is executed.

### HTML Template to Render the Log Content and the Plot (`templates/index.html`)
This HTML template displays the log content and the visualization plot.

#### Explanation:

- The template uses HTML to structure the page.
- `{% for line in log_content %} ... {% endfor %}`: A Jinja2 template loop to iterate over and display each line of the log content passed from `app.py`.
- `<img src="/static/honeyfile_interactions.png" alt="Honeyfile Interactions">`: Embeds the visualization plot in the web page.
