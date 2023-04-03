# System Performance Monitor

A Python script to monitor system performance, including CPU, memory, and disk usage.

## Requirements

- Python 3
- psutil library

## Installation

Install the required library:

```shell
pip install psutil
```

## Usage

Run the script:

```shell
python performance_monitor.py

```

The script will display the CPU, memory, and disk usage every 60 seconds.

## Python Development Environment Setup

A Bash script is available to set up a Python virtual environment and install common Python packages.

### Requirements

- Python 3
- venv module

### Usage

Run the script:

```shell
bash setup_environment.sh
```

#### Activate the virtual environment:

```shell
source venv/bin/activate
```

for Windows:

```shell
venv\Scripts\activate
```

#### To deactivate the virtual environment, run:

```shell
deactivate
```