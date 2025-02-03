import psutil
import os
import sys
from tabulate import tabulate

def list_processes():
    """List all running processes."""
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            process_info = proc.info
            process_list.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list

def display_processes(process_list):
    """Display the list of processes in a tabular format."""
    headers = ["PID", "Name", "Status"]
    table = [[proc['pid'], proc['name'], proc['status']] for proc in process_list]
    print(tabulate(table, headers, tablefmt="grid"))

def terminate_process(pid):
    """Terminate a process by PID."""
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=3)
        print(f"Process {pid} terminated successfully.")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
        print(f"Error terminating process {pid}: {e}")

def main():
    """Main function to run the MegaPortal program."""
    while True:
        print("\nMegaPortal - Process Monitor and Terminator")
        print("1. List Processes")
        print("2. Terminate Process")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            processes = list_processes()
            display_processes(processes)
        elif choice == '2':
            pid = int(input("Enter PID of the process to terminate: "))
            terminate_process(pid)
        elif choice == '3':
            print("Exiting MegaPortal.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()