
#!/bin/bash

# Function to convert Chinese numbers to Arabic numerals
convert_chinese_to_arabic() {
    case "$1" in
        ?) echo -n "0" ;;
        ?) echo -n "1" ;;
        ?) echo -n "2" ;;
        ?) echo -n "3" ;;
        ?) echo -n "4" ;;
        ?) echo -n "5" ;;
        ?) echo -n "6" ;;
        ?) echo -n "7" ;;
        ?) echo -n "8" ;;
        ?) echo -n "9" ;;
        *) echo -n "$1" ;;
    esac
}

# Function to extract Chinese numbers from filename and convert them to Arabic numerals
extract_and_convert() {
    filename="$1"
    result=""
    current_number=""
    while IFS= read -rn1 char; do
        case "$char" in
            [[:digit:]])
                current_number+="$char"
                ;;
            [??????????])
                current_number+=$(convert_chinese_to_arabic "$char")
                ;;
            *)
                if [[ -n "$current_number" ]]; then
                    result+="$current_number"
                    current_number=""
                fi
                ;;
        esac
    done <<< "$filename"
    if [[ -n "$current_number" ]]; then
        result+="$current_number"
    fi
    echo "$result"
}

# Main script
for file in *; do
    if [[ -f "$file" ]]; then
        # Extract Chinese numbers and convert them to Arabic numerals
        numbers=$(extract_and_convert "$file")

        if [[ -n "$numbers" ]]; then
            # Create new filename with Arabic numerals
            new_filename="${numbers}.csv"
            mv "$file" "$new_filename"
            echo "Renamed '$file' to '$new_filename'"
        else
            echo "No Chinese numbers found in '$file'"
        fi
    fi
done
