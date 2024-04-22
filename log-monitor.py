import time
import re
from collections import Counter


def monitor_log_file(log_file, patterns, report_interval=10):
    print("Monitoring log file:", log_file)

    # Create a Counter object to store pattern counts
    pattern_counter = Counter()

    # Compile regular expressions for the patterns
    compiled_patterns = [re.compile(pattern) for pattern in patterns]

    last_report_time = time.time()

    try:
        # Continuously read and analyze new lines from the log file
        with open(log_file, 'r') as f:
            while True:
                line = f.readline()
                if line:
                    # Print the new log entry
                    print(line, end='')

                    # Check each pattern against the log entry
                    for pattern in compiled_patterns:
                        if pattern.search(line):
                            # Update pattern count
                            pattern_counter[pattern.pattern] += 1

                    # Check if it's time to generate a summary report
                    if time.time() - last_report_time >= report_interval:
                        # Generate and print summary report
                        print("\nSummary Report:")
                        for pattern, count in pattern_counter.items():
                            print(f"{pattern}: {count}")

                        # Reset counters and update last report time
                        pattern_counter.clear()
                        last_report_time = time.time()
                else:
                    time.sleep(1)  # Wait for new lines to be added to the log file
    except KeyboardInterrupt:
        print("Monitoring stopped.")


if __name__ == "__main__":
    log_file = r"C:\Users\DEEKSHITH NAIK L\Desktop\Zookeeper_2k.log"  # Update with the actual path to your log file
    # Specify patterns to count occurrences
    patterns = ['error', 'warning']  # Example: Count occurrences of 'error' and 'warning'
    monitor_log_file(log_file, patterns)
