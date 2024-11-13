import json

filename = 'input.json'


def task(json_file) -> float:
    with open(json_file) as file:
        data = json.load(file)

    sum_of_div = sum(elem["score"] * elem["weight"] for elem in data)
    return round(sum_of_div, 3)


print(task(filename))
