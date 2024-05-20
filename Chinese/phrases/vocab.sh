
test_phrases() {
    local file="$HOME/Documents/2024-Notes/Chinese/phrases/vocabulary_bank.md"
    local incorrect_file="$HOME/Documents/2024-Notes/Chinese/phrases/incorrect_phrases.md"

    # Ensure the incorrect phrases file exists with the correct headers
    if [ ! -f "$incorrect_file" ]; then
        echo "| Phrase | Pinyin | Meaning |" > "$incorrect_file"
        echo "|------|------|---------|" >> "$incorrect_file"
    fi

    # Determine the source of phrases: incorrect file if not empty, otherwise main file
    if [ "$(wc -l < "$incorrect_file")" -gt 2 ]; then
        # Read incorrect phrases into an array
        IFS=$'\n' read -d '' -r -A phrases < <(tail -n +3 "$incorrect_file" | gshuf | head -n 20 && printf '\0')
    else
        # Read phrases from the main file into an array
        IFS=$'\n' read -d '' -r -A phrases < <(tail -n +3 "$file" | gshuf | head -n 20 && printf '\0')
    fi

    # Arrays to hold correct and incorrect phrases
    local correct_phrases=()
    local incorrect_phrases=()

    for phrase in "${phrases[@]}"; do
        # Extract the phrase and the correct meaning
        local word=$(echo "$phrase" | awk -F'|' '{print $2}' | xargs)
        local pinyin=$(echo "$phrase" | awk -F'|' '{print $3}' | xargs)
        local correct_meaning=$(echo "$phrase" | awk -F'|' '{print $4}' | xargs)

        # Prompt the user for the meaning
        echo "What is the meaning of: $word ($pinyin)?"
        read -r user_meaning

        # Check if the user's meaning matches the correct meaning
        if [[ "$user_meaning" == "$correct_meaning" ]]; then
            echo "Correct!"
            correct_phrases+=("$phrase")
        else
            echo "Incorrect. The correct meaning is: $correct_meaning"
            incorrect_phrases+=("$phrase")
        fi
    done

    # Print the results
    echo
    echo "Correct phrases:"
    for correct in "${correct_phrases[@]}"; do
        echo "$correct"
    done

    echo
    echo "Incorrect phrases:"
    for incorrect in "${incorrect_phrases[@]}"; do
        echo "$incorrect"
    done

    # Update the incorrect phrases file
    if [ ${#incorrect_phrases[@]} -gt 0 ]; then
        # Overwrite the incorrect phrases file with the new incorrect phrases
        echo "| Phrase | Pinyin | Meaning |" > "$incorrect_file"
        echo "|------|------|---------|" >> "$incorrect_file"
        for incorrect in "${incorrect_phrases[@]}"; do
            echo "$incorrect" >> "$incorrect_file"
        done
    else
        # Clear the incorrect phrases file if there are no incorrect phrases
        echo "| Phrase | Pinyin | Meaning |" > "$incorrect_file"
        echo "|------|------|---------|" >> "$incorrect_file"
    fi
}

edit_row_in_md() {
    local phrase=$1
    local meaning=$2
    local file="$HOME/Documents/2024-Notes/Chinese/phrases/vocabulary_bank.md"

    # Use sed to edit the row with the given phrase
    sed -i '' "s/^| $phrase | .* |$/| $phrase | $meaning |/" "$file"

    echo "Row edited in $file with phrase: $phrase"
}
# Function to add a row to a markdown file
select_from_md() {
    local search_term=$1
    local file="$HOME/Documents/2024-Notes/Chinese/phrases/vocabulary_bank.md"

    # Use ripgrep to search for the term in the file
    rg -i -N "$search_term" "$file"
}

# Function to delete a row from the markdown "database"
delete_row_from_md() {
    local phrase=$1
    local file="$HOME/Documents/2024-Notes/Chinese/phrases/vocabulary_bank.md"

    # Use sed to delete the row with the given phrase
    sed -i '' "/^| *$phrase .* |/d" "$file"

    echo "Row deleted from $file with phrase: $phrase"
}

# Function to add or search for entries in the markdown "database"
vocab() {
    local add_flag=false
    local delete_flag=false
    local open_flag=false
    local test_flag=false

    # Parse options
    while getopts ":adot" opt; do
        case ${opt} in
            a )
                add_flag=true
                ;;
            d )
                delete_flag=true
                ;;
            o)
                open_flag=true
                ;;
            t)
                test_flag=true
                ;;

            \? )
                echo "Invalid option: -$OPTARG" >&2
                return 1
                ;;
            : )
                echo "Option -$OPTARG requires an argument." >&2
                return 1
                ;;
        esac
    done
    shift $((OPTIND -1))

    if [ "$add_flag" = true ]; then
        local phrase=$1
        local pinyin=$2
        local meaning=$3
        local file="$HOME/Documents/2024-Notes/Chinese/phrases/vocabulary_bank.md"

        # Check if the file exists, if not create it with header
        if [ ! -f "$file" ]; then
            echo "| Phrase | Pinyin | Meaning |" > "$file"
            echo "|------|------|---------|" >> "$file"
        fi

        # Append new row
        echo "| $phrase | $pinyin | $meaning |" >> "$file"

        echo "New row added to $file:"
        echo "| $phrase | $pinyin | $meaning |"
    elif [ "$delete_flag" = true ]; then
        local phrase=$1
        delete_row_from_md "$phrase"
    elif [ "$open_flag" = true ]; then
        cd ~/Documents/2024-Notes/Chinese/phrases
        nvim vocabulary_bank.md -c ":TableModeRealign"
    elif [ "$test_flag" = true ]; then
        test_phrases
    else
        # No flags or invalid flags, search for entries
        select_from_md "$@"
    fi
}
