# MegaPortal

MegaPortal is a simple Python program that provides an interface to monitor and terminate unresponsive processes on Windows. This tool leverages the `psutil` library to interact with system processes.

## Features

- List all running processes with their PID, name, and status.
- Terminate unresponsive or unwanted processes by entering their PID.
- Simple command-line interface for ease of use.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Clone this repository to your local machine.
2. Install the `psutil` library if you haven't already:

   ```bash
   pip install psutil
   ```

3. Run the program:

   ```bash
   python MegaPortal.py
   ```

## Usage

1. Run the `MegaPortal.py` script.
2. Choose option `1` to list all running processes.
3. Choose option `2` to terminate a process by entering its PID.
4. Choose option `3` to exit the program.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

Use this tool at your own risk. Terminating critical system processes can lead to system instability. Ensure you know what process you're terminating.