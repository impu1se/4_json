import json
import argparse


def load_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


def converts_to_pretty(file_stream):
    return json.dumps(file_stream, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pretty print for JSON')
    parser.add_argument('-file', dest='filepath',
                        help='Input filepath and filename with expansion json')
    args = parser.parse_args()
    try:
        print(converts_to_pretty(load_file(args.filepath)))
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Не правильный формат файла')
