import os
import json
import re
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

flutter_dir = './api_flutter_dev/flutter'
snippets_dir = './api_flutter_dev/snippets'
output_json_path = './api_flutter_dev.json'

structured_data = []

def count_html_files(directory):
    logging.info('Counting HTML files...')
    count = 0
    for _, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                count += 1
    logging.info(f'Found {count} HTML files.')
    return count

# Count the total number of HTML files
total_html_files = count_html_files(flutter_dir)

def extract_text_and_title_from_html(html_file):
    logging.info(f'Extracting text and title...')
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else None
        # Remove script and useless elements
        for tag in soup(['nav', 'footer', 'script', 'style', 'noscript', 'svg']):
            tag.decompose()
        # Get text
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text, title

def extract_dart_references(html_file):
    logging.info(f'Extracting Dart references...')
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()
        # Find all occurrences of Dart file references
        dart_references = set()
        pattern = re.compile(r'<a name="([\w.]+?)"></a>\s<div class="snippet')
        matches = pattern.finditer(content)
        for match in matches:
            dart_file_name = match.group(1) + '.dart'
            dart_references.add(dart_file_name)
        logging.info(f'Found {len(dart_references)} Dart references.')
        return dart_references

def clean_dart_code(dart_file):
    with open(dart_file, 'r', encoding='utf-8') as file:
        code = file.read()
        # Here you can add more cleaning steps if needed
        return code

def process_html_file(root, html_file):
    html_file_path = os.path.join(root, html_file)
    relative_path = html_file_path.split('flutter_docs/flutter/')[-1]
    url = "https://api.flutter.dev/" + relative_path.replace(os.path.sep, '/')
    text_content, title = extract_text_and_title_from_html(html_file_path)

    dart_references = extract_dart_references(html_file_path)
    dart_files_content = []
    if dart_references:  # Check if there are Dart file references
        for dart_ref in dart_references:
            dart_file_name = dart_ref.rsplit('.', 1)[0] + '.dart'
            for dart_root, _, dart_files in os.walk(snippets_dir):
                if dart_file_name in dart_files:
                    dart_file_path = os.path.join(dart_root, dart_file_name)
                    dart_code = clean_dart_code(dart_file_path)
                    dart_files_content.append(dart_code)
    code_examples = dart_files_content if len(dart_files_content) > 0 else None
    item = {
        'url': url,
        'title': title,
        'documentation_content': text_content,
        'code_examples': code_examples,
    }
    logging.info(f'Item: {item}')
    structured_data.append(item)

def process_flutter_directory(flutter_dir):
    logging.info('Processing Flutter directory...')
    processed_files = 0
    for root, _, files in os.walk(flutter_dir):
        logging.info(f'Processing {root}...')
        html_files = [file for file in files if file.endswith('.html')]
        if not html_files:  # Skip directories without HTML files
            continue
        for html_file in html_files:
            processed_files += 1
            percent_complete = (processed_files / total_html_files) * 100
            logging.info(f'Processing HTML file: {html_file} ({processed_files}/{total_html_files}, {percent_complete:.2f}%)')
            process_html_file(root, html_file)

def remove_empty_fields(data_dict):
    return {k: v for k, v in data_dict.items() if v is not None and v != ''}

def remove_items_with_one_or_less_fields(data):
    return [item for item in data if len(item) > 1]

def remove_items_without_code_examples(data):
    return [item for item in data if item['code_examples'] is not None]

def save_to_jsons(output_path, data, max_file_size_mb=1):
    logging.info(f'Saving data to JSON files...')
    file_index = 1
    current_batch = []
    for item in data:
        current_batch.append(item)
        json_data = json.dumps(current_batch, indent=1)
        estimated_size = len(json_data.encode('utf-8')) / (1024 * 1024)  # Size in MB

        # Write to file if size exceeds limit or it's the last item
        if estimated_size > max_file_size_mb or item == data[-1]:
            current_file_path = output_path.replace('.json', f'_{file_index}.json')
            logging.info(f'Writing to file: {current_file_path}')
            with open(current_file_path, 'w', encoding='utf-8') as file:
                file.write(json_data)
            file_index += 1
            current_batch = []  # Reset batch for next file
        


# Process the Flutter directory
process_flutter_directory(flutter_dir)

# # Remove empty fields
# structured_data = [remove_empty_fields(data) for data in structured_data]

# # Remove items with one or less fields
# structured_data = remove_items_with_one_or_less_fields(structured_data)

# Remove items without code examples
structured_data = remove_items_without_code_examples(structured_data)

# Sort the data by URL
structured_data.sort(key=lambda x: x['url'])

# Save the structured data to a JSON file
save_to_jsons(output_json_path, structured_data)

logging.info('Data processing complete.')
