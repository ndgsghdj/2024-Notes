#!/bin/bash

# Path to the timetable
TIMETABLE_PATH="$HOME/Documents/2024-Notes/timetable.md"

# Current day and time
CURRENT_DAY=$(date +'%A')
CURRENT_TIME=$(date +'%H:%M')

# Read the timetable and find the corresponding subject and description
REMINDER=$(awk -v day="$CURRENT_DAY" -v time="$CURRENT_TIME" '
BEGIN { FS="|"; OFS="|" }
NR > 2 {
    gsub(/^[ \t]+|[ \t]+$/, "", $2);  # Trim whitespace
    gsub(/^[ \t]+|[ \t]+$/, "", $3);
    gsub(/^[ \t]+|[ \t]+$/, "", $4);
    gsub(/^[ \t]+|[ \t]+$/, "", $5);
    if ($2 == day && $3 == time) {
        print $4, $5;
        exit;
    }
}' "$TIMETABLE_PATH")

# Send notification if a subject is found
if [ -n "$REMINDER" ]; then
    SUBJECT=$(echo "$REMINDER" | cut -d '|' -f 1)
    DESCRIPTION=$(echo "$REMINDER" | cut -d '|' -f 2)
    terminal-notifier -title "Study Reminder" -message "It's time to study $SUBJECT: $DESCRIPTION"
fi
