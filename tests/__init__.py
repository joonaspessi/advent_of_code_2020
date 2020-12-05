import json


def get_event_input(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
        lines = []
        for line in input_data.splitlines():
            lines.append(line)

    print({"input": lines})
    return {
        "body": json.dumps({"input": lines})
    }


def get_event_input_raw(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
        return {
            "body": input_data
        }
