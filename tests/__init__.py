import json


def get_event_input_raw(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
        return {
            "body": input_data
        }
