import json


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day8/input.txt", 'r') as f:
            lines = f.readlines()
    return lines


def compute(prog_counter, acc, instructions):
    instruction = instructions[prog_counter]
    if instruction[:3] == 'nop':
        return (prog_counter + 1, acc)

    if instruction[:3] == 'acc' and instruction[4:5] == '+':
        return (prog_counter + 1, acc + int(instruction[5:]))

    if instruction[:3] == 'acc' and instruction[4:5] == '-':
        return (prog_counter + 1, acc - int(instruction[5:]))

    if instruction[:3] == 'jmp' and instruction[4:5] == '+':
        return (prog_counter + int(instruction[5:]), acc)

    if instruction[:3] == 'jmp' and instruction[4:5] == '-':
        return (prog_counter - int(instruction[5:]), acc)

    raise Exception("malformed program")


def flip_nop_jmp(counter, instructions):
    new_instructions = instructions[:]
    instruction = new_instructions[counter]
    if instruction[:3] == 'jmp':
        instruction = instruction.replace("jmp", "nop")
    elif instruction[:3] == 'nop':
        instruction = instruction.replace("nop", "jmp")
    new_instructions[counter] = instruction

    return new_instructions


def lambda_handler(event, _):
    """Advent of code day 8, excercise 1
    """
    instructions = get_input(event)
    acc = 0
    prog_counter = 0
    computed = set()

    while True:
        if prog_counter in computed:
            break
        computed.add(prog_counter)
        prog_counter, acc = compute(prog_counter, acc, instructions)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": acc
        }),
    }


def lambda_handler_2(event, _):
    """Advent of code day 8, excercise 2
    """
    original_instructions = get_input(event)

    for index, _ in enumerate(original_instructions):
        instructions = flip_nop_jmp(index, original_instructions)
        acc = 0
        prog_counter = 0
        computed = set()
        try:
            while True:
                if prog_counter in computed:
                    break
                computed.add(prog_counter)
                prog_counter, acc = compute(prog_counter, acc, instructions)
                if prog_counter == len(original_instructions):
                    break
        except:
            continue
        if prog_counter == len(original_instructions):
            break

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": acc
        }),
    }
