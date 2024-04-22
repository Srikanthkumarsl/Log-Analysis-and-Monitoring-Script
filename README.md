# Log Analysis and Monitoring Script
# What is Log file?
log file keeps a record of event detail, date and time, this is generally used by the antivirus, your OS, and Apps to track some unusual activity or errors.

# What is log analysis?
•	Process of interpreting computer-generated records called log

•	Involves a large amount of data, depending on the scope of technology in the evaluation

•	Gives visibility into the performance and health of IT infrastructure and application stacks

# What is Log Monitoring?
•	The act of reviewing collected as they are recorded

•	Involves aggregating log file and providing alerts or notification for particular log messages and events

•	Involves the assistance of log management software

# How to use and test the script

# 1.	Setup:

•	Ensure you have Python installed on your system. You can download it from the official Python website if you haven't already: https://www.python.org/downloads/

•	Save the script provided in the previous message to a Python (.py) file, for example, log_monitor.py.

•	Prepare a sample log file (or use an existing one) that contains entries in the format expected by the script.

# 2.	Customize:

•	If necessary, customize the regular expression pattern in the parse_log_entries function to match the format of your log entries. Adjust the pattern to extract the timestamp and message appropriately.

•	Update the log_file_path variable with the path to your sample log file.

# 3.	Run the Script:

•	Open a terminal or command prompt.

•	Navigate to the directory containing the script (log_monitor.py).

•	Run the script by executing the command: python log_monitor.py

# 4. To Stop monitoring

• When you run this script (log_monitor.py), it will continuously monitor the specified log file for new entries. Pressing Ctrl+C  will trigger the signal handler, which stops the monitoring loop gracefully.

# 5.	Verify Output:

•	The script will read the log file, parse the log entries, and store them in a list of dictionaries (parsed_entries).

•	Check the output to ensure that the log entries are parsed correctly and that the timestamps and messages are extracted accurately.

# 6.	Testing:

•	Test the script with different log files containing various types of log entries to ensure that it handles different formats correctly.

•	Create test cases to cover different scenarios, such as log entries with missing timestamps or unexpected formats.

•	Verify that the script behaves as expected and produces the desired output in each scenario.

# 7.	Error Handling:

•	Introduce deliberate errors in the log file or modify the script to handle unexpected situations, such as invalid log entries or missing log files.

•	Ensure that the script gracefully handles errors and exceptions without crashing or producing incorrect results.

# 8.	Performance Testing:

•	Test the script with large log files to evaluate its performance and efficiency.

•	Monitor resource usage (CPU, memory) to identify any potential bottlenecks or performance issues.

•	Optimize the script if necessary to improve its speed and resource efficiency.

# 9.	Documentation:

•	Document the usage of the script, including any dependencies, configuration options, and command-line arguments.

•	Provide clear instructions on how to run the script and interpret the output.

•	Include examples and sample command lines to illustrate usage in different scenarios.
 
