import json
import re

def get_data_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def remove_field_from_data(data, field):
    for item in data:
        item.pop(field, None)
    return data

def remove_item_where_regex_matches(data, field, regex):
    return [item for item in data if not regex.match(item[field])]

def save_to_json(output_path, data):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


data = get_data_from_json('dart_dev.json')
data = remove_field_from_data(data, 'metadata')
data.sort(key=lambda x: x['url'])
save_to_json('dart_dev_clean.json', data)


data = get_data_from_json('docs_flutter_dev.json')
data = remove_field_from_data(data, 'metadata')
data.sort(key=lambda x: x['url'])
save_to_json('docs_flutter_dev_clean.json', data)


data = get_data_from_json('riverpod_dev.json')
data = remove_field_from_data(data, 'metadata')
data = remove_item_where_regex_matches(data, 'url', re.compile(r'^https://riverpod\.dev/../'))
data.sort(key=lambda x: x['url'])
save_to_json('riverpod_dev_clean.json', data)

