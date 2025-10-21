# import re
# from collections import Counter

# def analyze_log(log_text):
#     errors = re.findall(r"(?i)error.*", log_text)       # (?i) = case-insensitive
#     warnings = re.findall(r"(?i)warn.*", log_text)

#     summary = {
#         "total_errors": len(errors),
#         "total_warnings": len(warnings),
#         "top_errors": Counter(errors).most_common(5)
#     }
#     return summary


import re
from collections import Counter
import datetime

# Pattern examples (you can tune them for your log format)
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}[\sT]\d{2}:\d{2}:\d{2}).*?(?P<level>ERROR|WARNING|INFO).*?(?P<message>.+)'
)

def analyze_log(log_text):
    """
    Analyzes log text to detect patterns, frequency, and trends.
    """
    entries = []
    for match in LOG_PATTERN.finditer(log_text):
        entry = match.groupdict()
        entries.append(entry)

    if not entries:
        return {"message": "No valid log entries found."}

    # Count frequency of levels
    level_counts = Counter([e["level"] for e in entries])

    # Most common messages (e.g. top errors)
    top_messages = Counter([e["message"].strip() for e in entries if e["level"] == "ERROR"]).most_common(5)

    # Extract timeline data (optional)
    timestamps = [e["timestamp"] for e in entries]
    if timestamps:
        start_time = timestamps[0]
        end_time = timestamps[-1]
    else:
        start_time = end_time = None

    # Output summary
    summary = {
        "total_entries": len(entries),
        "level_counts": dict(level_counts),
        "top_errors": [{"message": msg, "count": count} for msg, count in top_messages],
        "time_range": {"start": start_time, "end": end_time},
    }

    return summary
