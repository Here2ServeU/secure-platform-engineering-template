# Script to summarize logs using GPT
import sys
import re
from collections import Counter

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def summarize_log(file_path):
    level_counter = Counter()
    log_level_pattern = re.compile(r"\b({})\b".format("|".join(LOG_LEVELS)))
    with open(file_path, "r") as f:
        for line in f:
            match = log_level_pattern.search(line)
            if match:
                level_counter[match.group()] += 1
    return level_counter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log-summarizer.py <log-file>")
        sys.exit(1)
    log_file = sys.argv[1]
    try:
        summary = summarize_log(log_file)
        print("Log Summary:")
        for level in LOG_LEVELS:
            print(f"{level}: {summary.get(level, 0)}")
        sys.exit(0)
    except Exception as e:
        print(f"Failed to summarize log: {e}")
        sys.exit(2)