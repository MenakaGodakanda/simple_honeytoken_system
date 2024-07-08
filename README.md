# Simple Honeytoken System

The Simple Honeytoken System is a security project designed to create a decoy file (honeyfile), monitor interactions with it, log those interactions, and visualize the log data. This project aims to detect unauthorized access or suspicious activities by using open-source tools.

## Overview
<img width="1391" alt="Screenshot 2024-07-08 at 8 24 17 PM" src="https://github.com/MenakaGodakanda/simple_honeytoken_system/assets/156875412/a2665012-830f-4836-b9ba-3ec3c2aebf77">

### Explanation:
1. **File Creation**:
    - `honeyfile.txt` is created and placed in the project directory.
2. **File Monitoring**:
    - `monitor.py` runs and uses `inotifywait` to watch `honeyfile.txt`.
    - Interactions with `honeyfile.txt` are logged into `logs/honeyfile_log.txt`.
3. **Log Visualization**:
    - `visualize.py` reads `logs/honeyfile_log.txt` and generates a visualization.
    - The visualization is saved as `static/honeyfile_interactions.png`.
4. **Web Interface**:
    - `app.py` sets up a Flask web server.
    - The server serves the log content and the visualization plot.
    - Users can view the log and the plot through their web browser.

## Features

- **Honeyfile Creation**: A decoy file (`honeyfile.txt`) with fake sensitive information.
- **File Monitoring**: Continuous monitoring of the honeyfile for any interactions using `inotifywait`.
- **Logging**: Records interactions in a log file.
- **Visualization**: Generates a visual representation of interactions over time.
- **Web Interface**: Displays the log and the visualization through a simple Flask web application.

## Setup Instructions

### Prerequisites

- **Operating System**: Linux (Ubuntu recommended)
- **Python**: Version 3.6 or higher
- **Packages**: `inotify-tools`, `matplotlib`, `flask`

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/MenakaGodakanda/simple_honeytoken_system.git
cd simple_honeytoken_system
```

2. **Install Required Packages**

```bash
sudo apt-get update
sudo apt-get install inotify-tools
pip install matplotlib flask
```

## Usage
1. **Start Monitoring**
- The `monitor.py` script will use inotifywait to monitor the honeyfile for any interactions and log them.
- In one terminal, start the monitoring script.
```bash
python3 monitor.py
```

2. **Generate Visualization**
- The `visualize.py` script will read the log file and create a visualization of the interactions.
- In another terminal, periodically run the following command to update the visualization plot:

```bash
python3 visualize.py
```
- Output should look like this:<br><br>
![honeyfile_interactions](https://github.com/MenakaGodakanda/simple_honeytoken_system/assets/156875412/e3cb04ae-c304-4d83-924b-2b5bc94cf49a)

3. **Start the Web Server**
- The `app.py` script will create a simple web server to display the log and the visualization.
```bash
python3 app.py
```
- Output should look like this:<br><br>
![Screenshot 2024-07-08 200617](https://github.com/MenakaGodakanda/simple_honeytoken_system/assets/156875412/a0fd0c4d-5ad3-4313-ae2d-bb2290d7bd51)

4. **View Logs and Visualization**
- Open your web browser and navigate to `http://127.0.0.1:5000/` to view the log content and the visualization plot.
- Output of the web browser showing `Logs of Interactions`:<br><br>
![Screenshot 2024-07-08 203312](https://github.com/MenakaGodakanda/simple_honeytoken_system/assets/156875412/de6cb5b0-b566-4a0f-98bf-e3c2b1ca527b) <br><br><br>
- Output of the web browser showing `Interaction Visualization`:<br><br>
![Screenshot 2024-07-08 203320](https://github.com/MenakaGodakanda/simple_honeytoken_system/assets/156875412/91fda2f9-a386-4417-9733-64ebf6f4515f)
## Directory Structure
```
simple_honeytoken_system/
├── app.py                            # Flask web application script
├── logs/                             # Directory for log files
│ └── honeyfile_log.txt               # Log file for recording interactions
├── monitor.py                        # Script to monitor interactions with honeyfile.txt
├── static/                           # Directory for static files
│ └── honeyfile_interactions.png      # Visualization plot
├── templates/                        # Directory for HTML templates
│ └── index.html                      # HTML template for the web interface
├── visualize.py                      # Script to generate visualization from log data
└── honeyfile.txt                     # Decoy file with fake data
```

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
