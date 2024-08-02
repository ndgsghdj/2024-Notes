import re
import os
import sys

def split_markdown_file(input_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Regular expression to find headers (ignoring # headers)
    header_regex = re.compile(r'^(#{2,6})\s+(.*)', re.MULTILINE)

    # Find all headers in the content
    headers = header_regex.findall(content)

    # Split the content based on headers
    sections = header_regex.split(content)

    # Combine headers and their respective contents
    combined_sections = []
    current_section = None
    current_level = 0

    for i in range(1, len(sections), 3):
        header = sections[i]
        level = len(header)
        title = sections[i+1].strip().replace(' ', '_')
        text = sections[i+2]

        if current_section is None:
            current_section = (header, title, text)
            current_level = level
        else:
            if level <= current_level:
                combined_sections.append(current_section)
                current_section = (header, title, text)
                current_level = level
            else:
                current_section = (current_section[0], current_section[1], current_section[2] + header + ' ' + sections[i+1] + '\n' + text)

    if current_section is not None:
        combined_sections.append(current_section)

    # Create an output directory
    output_dir = f"Events/{input_file}".split(".")[0]
    os.makedirs(output_dir, exist_ok=True)

    # Write each section to its own Markdown file
    for i, (header, title, text) in enumerate(combined_sections):
        output_file = os.path.join(output_dir, f'{title}.md')
        with open(output_file, 'w') as file:
            file.write(header + ' ' + title.replace('_', ' ') + '\n' + text)

    print(f"Markdown file split into {len(combined_sections)} sections.")

# Replace 'your_markdown_file.md' with the path to your Markdown file

split_markdown_file(sys.argv[1])
