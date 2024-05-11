'''
Task 3
--------------------------------------------------------------------------------------------

Develop a Python script for analyzing log files. The script should be able to read a log file 
passed as a command line argument and display statistics by logging levels, such as INFO, ERROR, DEBUG. 
Additionally, users can specify a logging level as a second command line argument to retrieve all entries of that level.

Log files are files that contain records of events that have occurred in an operating system, software, 
or other systems. They help track and analyze system behavior, identify, and diagnose problems.

For this task, consider the following example of a log file:

2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.

Task Requirements:

• The script should accept the path to a log file as a command line argument.
• The script should accept an optional command line argument following the log file path argument. 
  It is responsible for displaying all entries of a specific logging level. For example, the argument "error" 
  will display all ERROR level entries from the log file.
• The script must read and analyze the log file, counting the number of entries for each logging level 
  (INFO, ERROR, DEBUG, WARNING).
• Implement the function parse_log_line(line: str) -> dict for parsing log lines.
• Implement the function load_logs(file_path: str) -> list for loading logs from a file.
• Implement the function filter_logs_by_level(logs: list, level: str) -> list for filtering logs by level.
• Implement the function count_logs_by_level(logs: list) -> dict for counting entries by logging level.
• Results should be presented in a table format showing the number of entries for each level. 
  For this, implement the function display_log_counts(counts: dict), which formats and displays the results. 
  It accepts the results from the function count_logs_by_level.

Execution Recommendations:

• Before starting, familiarize yourself with the structure of your log file. Pay attention to the date and time format, logging levels (INFO, ERROR, DEBUG, WARNING), and the structure of messages.
• Understand how different components of the log are separated, usually by spaces or special characters.
• Break down your task into logical blocks and functions for better readability and future expansion.
• Parsing a log line is done by the parse_log_line(line: str) -> dict function, which takes a line from the log as input and returns a dictionary with parsed components: date, time, level, message. Use string methods such as split() to divide the line into parts.
• Loading log files is performed by the load_logs(file_path: str) -> list function, which opens the file, reads each line, and applies the parse_log_line function to it, storing the results in a list.
• Filtering by logging level is done by the filter_logs_by_level(logs: list, level: str) -> list. It allows you to obtain all log entries for a specific logging level.
• Counting entries by logging level should be done by the count_logs_by_level(logs: list) -> dict, which goes through all entries and counts the number of entries for each logging level.
• Displaying results is done using the display_log_counts(counts: dict) function, which formats and presents the count results in a readable format.
• Your script should be able to handle various kinds of errors, such as missing files or errors during reading. Use try/except blocks to handle exceptional situations.

Evaluation Criteria:

• The script performs all specified requirements, correctly analyzing log files and displaying information.
• The script correctly handles errors, such as incorrect log file format or missing file.
• The development must have used an element of functional programming: lambda function, list comprehension, filter function, etc.
• The code is well-structured, understandable, and contains comments where necessary.

Example of Use:

When running the script

python main.py /path/to/logfile.log

You should expect the following output:

Logging Level | Count
--------------|------
INFO          | 4
DEBUG         | 3
ERROR         | 2
WARNING       | 1

If the user wants to view all entries of a specific logging level, they can run the script with 
an additional argument, for example:

python main.py /path/to/logfile.log error

This will display the overall statistics by levels, as well as detailed information for all entries of the ERROR level.

Logging Level | Count
--------------|------
INFO          | 4
DEBUG         | 3
ERROR         | 2
WARNING       | 1

Log Details for 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
'''

import sys
import re
from collections import defaultdict

# Parses a single log line and returns its components as a dictionary.
def parse_log_line(line: str) -> dict:
    # Use regex to split the line into components assuming standard log format: "DATE TIME LEVEL MESSAGE"
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)', line)
    if match:
        return {
            'date_time': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return {}

# Loads log entries from a file and parses each line.
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    return logs

# Filters logs by a specific logging level.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]

# Counts the number of log entries for each level.
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

# Displays the counts of log entries by level in a tabular format.
def display_log_counts(counts: dict):
    print("Logging Level | Count")
    print("--------------|------")
    for level, count in sorted(counts.items()):
        print(f"{level:13} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    # Display counts for all levels first
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        filtered_counts = count_logs_by_level(filtered_logs)
        print(f"\nDetails for level '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date_time']} - {log['message']}")
    else:
        display_log_counts(counts)

# Navigate to `03-logs-file-analyzer` Directory and run command, for example: `python main.py logfile.log warning`
if __name__ == "__main__":
    main()
