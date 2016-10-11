import sys
import json
import argparse


parser = argparse.ArgumentParser(description='Pretty print for JSON')
parser.add_argument('-file', dest='filepath',
                    help='Input filepath and filename with expansion json' )
args = parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        print('Файл не найден')
        sys.exit(1)


def pretty_print_json(data):
    return print(json.dumps(data, indent=4))


if __name__ == '__main__':
    open_file = load_data(args.filepath)
    pretty_print_json(open_file)
