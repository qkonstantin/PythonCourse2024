import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    delimiter = ','
    quotechar = '\n'
    indent = 4

    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter=delimiter, quotechar=quotechar)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(data, file, indent=indent)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
