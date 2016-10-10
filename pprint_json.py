import sys
import json


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Файл не найден')
        sys.exit(1)



def pretty_print_json(data):
    result = None
    if isinstance(data, list):
        result = ['[\n\t']
        for i in data:
            if isinstance(i, dict):
                result += '{\n\t' + i + ':'
                for key, value in i:
                    while isinstance(value, dict):






if __name__ == '__main__':
    open_file = load_data('magazine.json')
    pretty_print_json(open_file)
