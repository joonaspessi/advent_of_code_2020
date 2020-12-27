import json
import fileinput
import re


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        return fileinput.input()
    return lines


def process_line(line):
    stack = []
    found = True
    calc = line
    while found:
        found = False
        print(calc)
        for i, c in enumerate(calc):
            if c == "(":
                stack.append(i)
                found = True
            if c == ")":
                start = stack.pop()
                if len(stack) == 0:
                    res = process_line(calc[start + 1: i])
                    print(res)
                    calc = calc[:start] + res + calc[i + 1:]
                    break
        if not found:
            break

    operators = re.findall(r"[\*|+]+", calc)
    elements = re.findall(r"\d+", calc)

    print(operators, elements)
    result = int(elements.pop(0))
    for _ in range(len(elements)):
        op = operators.pop(0)
        b = elements.pop(0)
        print(result, op, b)
        if op == "*":
            result *= int(b)
        if op == "+":
            result += int(b)
    print(result)
    return str(result)


def process_line_2(line):
    stack = []
    found = True
    calc = line

    while found:
        found = False
        for i, c in enumerate(calc):
            if c == "(":
                stack.append(i)
                found = True
            if c == ")":
                start = stack.pop()
                if len(stack) == 0:
                    res = process_line_2(calc[start + 1: i])
                    calc = calc[:start] + res + calc[i + 1:]
                    break
        if not found:
            break

    operators = re.findall(r"[\*|+]+", calc)
    elements = re.findall(r"\d+", calc)
    print("calculating:", calc, operators, elements)

    print(operators, elements)

    print(operators, elements)
    result = int(elements.pop(0))
    for _ in range(len(elements)):
        op = operators.pop(0)
        b = elements.pop(0)
        print(result, op, b)
        if op == "*":
            result *= int(b)
        if op == "+":
            result += int(b)
    print(result)

    return str(result)


def precedence(op):
    if op == '+' or op == '-':
        return 2
    if op == '*' or op == '/':
        return 1
    return 0


def apply_op(op, a, b):
    print(op, a, b)
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b


def evaluate(tokens):
    values = []
    ops = []

    token_len = len(tokens)
    i = 0
    while i < token_len:
        print(values, ops)
        if tokens[i] == " ":
            i += 1
            continue
        elif tokens[i] == "(":
            ops.append(tokens[i])
        elif tokens[i].isdigit():
            val = 0
            while i < len(tokens) and tokens[i].isdigit():
                val = (val * 10) + int(tokens[i])
                i += 1
            values.append(int(val))
            i -= 1
        elif tokens[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(op, val2, val1))
            ops.pop()
        # operator
        else:
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(op, val2, val1))
            ops.append(tokens[i])
        i += 1

    while len(ops) > 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_op(op, val1, val2))

    return values[-1]


def lambda_handler(event, _):
    input = get_input(event)

    total = 0
    for line in input:
        print(line)
        total += int(process_line(line))

    print(total)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": total
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)

    total = 0
    for line in input:
        print(line)
        total += evaluate(line.strip())

    print(total)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": total
        })
    }


if __name__ == "__main__":
    lambda_handler_2({}, {})
