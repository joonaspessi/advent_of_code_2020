import json
import re


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open("day12/input.txt", 'r') as f:
            lines = f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    cons, _, nt = input.split("\n\n")
    reg = r"^(.+)\: (\d+)-(\d+) or (\d+)-(\d+)$"
    constrains = []
    for c in cons.splitlines():
        c = c.rstrip()
        res = re.search(reg, c)
        constrains.append(range(int(res[2]), int(res[3])+1))
        constrains.append(range(int(res[4]), int(res[5])+1))

    invalid_values = []
    for n in [(int(n)) for n in nt[nt.index(":") + 2:].replace("\n", ",").split(",")]:
        con_ok = False
        for c in constrains:
            if n in c:
                con_ok = True
        if not con_ok:
            invalid_values.append(n)
    result = sum(invalid_values)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }
