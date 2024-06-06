#!/bin/bash
TIMETABLE_PATH="$HOME/Documents/2024-Notes/timetable.md"
CRON_TMP_FILE="/tmp/cron_reminders.tmp"

# Function to convert day name to cron-compatible format
day_to_cron_day() {
    case $1 in
        Monday) echo 1 ;;
        Tuesday) echo 2 ;;
        Wednesday) echo 3 ;;
        Thursday) echo 4 ;;
        Friday) echo 5 ;;
        Saturday) echo 6 ;;
        Sunday) echo 0 ;;
    esac
}

export -f day_to_cron_day

# Clear any previous reminders to avoid duplicates
crontab -l | grep -v '# Study Reminder' > $CRON_TMP_FILE

# Read the timetable and add cron jobs
while IFS='|' read -r _ day time subject description _; do
    day=$(echo $day | xargs)  # Remove leading/trailing whitespace
    time=$(echo $time | xargs)  # Remove leading/trailing whitespace
    subject=$(echo $subject | xargs)  # Remove leading/trailing whitespace
    description=$(echo $description | xargs)  # Remove leading/trailing whitespace

    # Skip header or empty lines
    if [[ $day == "Day" || -z $day ]]; then
        continue
    fi

    cron_day=$(day_to_cron_day $day)
    hour=$(echo $time | cut -d':' -f1)
    minute=$(echo $time | cut -d':' -f2)

    command="/opt/homebrew/bin/terminal-notifier -sender com.apple.Terminal -activate com.apple.Terminal -title '$subject' -message '$description' -sound default -ignoreDnD"
    echo "$minute $hour * * $cron_day $command # Study Reminder" >> $CRON_TMP_FILE

done < <(tail -n +3 "$TIMETABLE_PATH")

# Install new cron file
crontab $CRON_TMP_FILE
rm $CRON_TMP_FILE

echo "Reminders have been added to your crontab."
