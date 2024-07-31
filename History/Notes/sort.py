import re

def extract_year(line):
    match = re.search(r'\b(\d{4})\b', line)
    return int(match.group(1)) if match else float('inf')

def sort_markdown_by_year(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines.sort(key=extract_year)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

if __name__ == "__main__":
    markdown_file_path = 'Timeline.md'
    sort_markdown_by_year(markdown_file_path)

