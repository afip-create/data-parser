# data-parser
# ===========

"""
Data Parser

This is a simple command-line tool for parsing CSV files.

Usage
-----

    $ python data-parser.py --help

    $ python data-parser.py --input data.csv --output parsed_data.json

"""
import argparse
import json

def parse_csv(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            data = []
            for line in input_file:
                row = line.strip().split(',')
                data.append({key: value for key, value in zip(['Name', 'Age', 'City'], row)})
            with open(output_filename, 'w') as output_file:
                json.dump(data, output_file)
    except FileNotFoundError:
        print("File not found.")

def main():
    parser = argparse.ArgumentParser(description="Data Parser")
    parser.add_argument('--input', type=str, help='Input CSV file name')
    parser.add_argument('--output', type=str, help='Output JSON file name')
    args = parser.parse_args()
    parse_csv(args.input, args.output)

if __name__ == "__main__":
    main()