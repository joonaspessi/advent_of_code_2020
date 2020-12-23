import json
import sys


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    print(input)
    

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    print(input)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lambda_handler({"fileName": sys.argv[1]}, {})
    else:
        lambda_handler_2({"fileName": sys.argv[1]}, {})
