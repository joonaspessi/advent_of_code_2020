import json


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    result = 0
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    result = 0
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


if __name__ == "__main__":
    lambda_handler({"fileName": sys.argv[1]}, {})
    # lambda_handler_2({"fileName": sys.argv[1]}, {})
