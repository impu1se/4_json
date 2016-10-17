import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
            return json.load(f)


def pretty_print_json(data):
    return json.dumps(data, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pretty print for JSON')
    parser.add_argument('-file', dest='filepath',
                        help='Input filepath and filename with expansion json')
    args = parser.parse_args()
    try:
        print(pretty_print_json(load_data(args.filepath)))
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Не правильный формат файла')
