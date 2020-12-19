import sys
import re
import json
import fileinput

R = {}
C = {}
DP = {}


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
        # return [l.strip() for l in fileinput.input()]
    return lines


def match_message_list(message, rules):
    if not message and not rules:
        return True
    if not message:
        return False
    if not rules:
        return False

    ret = False
    for i in range(len(message) + 1):
        if match_message(message[:i], rules[0]) and match_message_list(message[i:], rules[1:]):
            ret = True
    return ret


def match_message(message, rule):
    """ CKY algorithm
    """
    key = (message, rule)

    if key in DP:
        return DP[key]

    ret = False
    if rule in C:
        ret = (message == C[rule])
    else:
        for option in R[rule]:
            if match_message_list(message, option):
                ret = True
    DP[key] = ret
    return ret


def lambda_handler(event, _):
    input = get_input(event)

    rules, messages = input.split("\n\n")

    for rule in rules.splitlines():

        # end node
        if re.match(r'^(\d+): "([ab])"$', rule):
            match = re.search(r'^(\d+): "([ab])"$', rule)
            end_node_index = match.group(1)
            end_node_value = match.group(2)
            C[int(end_node_index)] = end_node_value
        else:
            node_index, conditions = rule.split(":")
            child = []
            for c in conditions.split("|"):
                child.append([int(x) for x in c.strip().split(" ")])
            R[int(node_index)] = child

    ans = 0
    for message in messages.splitlines():
        DP.clear()
        message = message.strip()
        if match_message(message, 0):
            ans += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": ans
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    rules, messages = input.split("\n\n")
    for rule in rules.splitlines():
        if re.match(r'^(\d+): "([ab])"$', rule):
            match = re.search(r'^(\d+): "([ab])"$', rule)
            end_node_index = match.group(1)
            end_node_value = match.group(2)
            C[int(end_node_index)] = end_node_value
        else:
            node_index, conditions = rule.split(":")
            child = []
            if node_index == "8":
                conditions = " 42 | 42 8"
            if node_index == "11":
                conditions = " 42 31 | 42 11 31"
            for c in conditions.split("|"):
                child.append([int(x) for x in c.strip().split(" ")])
            R[int(node_index)] = child

    ans = 0
    for message in messages.splitlines():
        DP.clear()
        message = message.strip()
        if match_message(message, 0):
            ans += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": ans
        })
    }


if __name__ == "__main__":
    lambda_handler_2({"fileName": sys.argv[1]}, {})
