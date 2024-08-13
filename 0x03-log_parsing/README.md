## 0x03. Log Parsing

## Project Overview
The 0x03. Log Parsing project is part of a short specialization in Python programming. The primary goal is to develop a Python script that reads log data from standard input (stdin), processes the data, and computes various metrics. This project involves parsing log entries, handling data streams, and generating statistics based on the log data.

## Objective
Write a Python script to read log entries from stdin and compute the following metrics:
- Total file size: The sum of all file sizes from log entries.
- Number of lines by status code: Counts of occurrences for specific status codes (200, 301, 400, 401, 403, 404, 405, 500).
- The script should print these statistics every 10 lines and/or upon receiving a keyboard interruption (CTRL + C).

## Concepts and Skills Required
- File I/O in Python: Read from sys.stdin line by line.
- Signal Handling in Python: Handle keyboard interruptions using signals.
- Data Processing: Parse and aggregate data from log entries.
- Regular Expressions: Validate log entry formats.
- Dictionaries in Python: Count occurrences of status codes and accumulate file sizes.
- Exception Handling: Manage exceptions during file reading and data processing.

## Resources
- Python Input and Output
- Python Signal Handling
- Python Regular Expressions
- Python Dictionaries
- Python Exceptions
