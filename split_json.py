import json
import logging

def get_data_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_to_jsons(output_path, data, max_file_size_mb=6.8):
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
            with open(current_file_path, 'w', encoding='utf-8') as file:
                file.write(json_data)
            file_index += 1
            current_batch = []  # Reset batch for next file

data = get_data_from_json('docs_flutter_dev.json')

save_to_jsons('docs_flutter_dev.json', data)
