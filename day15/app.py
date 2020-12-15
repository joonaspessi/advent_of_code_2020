import json


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open("day12/input.txt", 'r') as f:
            lines = f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    start = [int(n) for n in input.split(",")]

    mem = {}
    turns = []
    for s in start:
        turns.append(s)
        if s not in mem:
            mem[s] = []
        mem[s].append(len(turns))

    for turn in range(len(turns) + 1, 2020 + 1):
        prev = turns[-1]

        if prev not in turns[:-1]:
            turns.append(0)
            if 0 not in mem:
                mem[0] = []
            mem[0].append(turn)
        elif len(mem[prev]) >= 2:
            new_val = mem[prev][-1] - mem[prev][-2]
            turns.append(new_val)
            if new_val not in mem:
                mem[new_val] = []
            mem[new_val].append(turn)
        else:
            new_val = turn - mem[prev][0]
            turns.append(new_val)
            if new_val not in mem:
                mem[new_val] = []
            mem[new_val].append(turn)

    result = turns[-1:]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    start = [int(n) for n in input.split(",")]

    mem = {}
    turns = []
    for s in start:
        turns.append(s)
        if s not in mem:
            mem[s] = []
        mem[s].append(len(turns))

    for turn in range(len(turns) + 1, 30000000 + 1):
        prev = turns[-1]

        if prev not in turns[:-1]:
            turns.append(0)
            if 0 not in mem:
                mem[0] = []
            mem[0].append(turn)
        elif len(mem[prev]) >= 2:
            new_val = mem[prev][-1] - mem[prev][-2]
            turns.append(new_val)
            if new_val not in mem:
                mem[new_val] = []
            mem[new_val].append(turn)
        else:
            new_val = turn - mem[prev][0]
            turns.append(new_val)
            if new_val not in mem:
                mem[new_val] = []
            mem[new_val].append(turn)
