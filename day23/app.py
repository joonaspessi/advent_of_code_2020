import json
import sys


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def pick_up(cups, selected):
    cups_len = len(cups)
    start_index = cups.index(selected)
    picked = []
    for i in range(1, 4):
        picked.append(cups[(start_index + i) % cups_len])
    cups_without_selected = [n for n in cups if n not in picked]
    return picked, cups_without_selected


def destination_cup(cups, selected):
    max_cup = max(cups)
    min_cup = min(cups)

    while True:
        selected -= 1
        if selected < min_cup:
            print("here")
            selected = max_cup
        if selected in cups:
            break
    return selected


def insert_cups(cups, cups_insert,  destination):
    index = cups.index(destination)
    return cups[:index+1] + cups_insert + cups[index+1:]


def select_current_cup(cups, current_cup):
    cups_len = len(cups)
    index = (cups.index(current_cup) + 1) % cups_len
    return cups[index]


def get_cup_result(cups):
    index = cups.index(1)
    result_cups = cups[index+1:] + cups[:index]

    return "".join([str(c)for c in result_cups])


def print_cups(cups, selected):
    print('cups: ', end='')
    for c in cups:
        if c == selected:
            print(f"({c}) ", end='')
        else:
            print(f"{c} ", end='')
    print("")


def print_picked_cups(cups):
    print('pick up: ', end='')
    for c in cups:
        print(f"{c} ", end='')
    print("")


def lambda_handler(event, _):
    input = get_input(event)
    cups = [int(n) for n in input]
    current_cup = cups[0]
    destination = -1

    for move in range(0, 100):
        print(f"-- move {move+1} --")
        print_cups(cups, current_cup)
        picked, cups_wo = pick_up(cups, current_cup)
        print_picked_cups(picked)
        destination = destination_cup(cups_wo, current_cup)
        print("destination:", destination)
        cups = insert_cups(cups_wo, picked, destination)
        current_cup = select_current_cup(cups, current_cup)
        print("")

    print("-- final --")
    print_cups(cups, current_cup)
    print(get_cup_result(cups))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
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
    if len(sys.argv) == 2:
        lambda_handler({"fileName": sys.argv[1]}, {})
    else:
        lambda_handler_2({"fileName": sys.argv[1]}, {})
