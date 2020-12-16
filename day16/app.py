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
    cons, mt, nt = input.split("\n\n")
    reg = r"^(.+)\: (\d+)-(\d+) or (\d+)-(\d+)$"
    constrains = []
    rules = {}
    for c in cons.splitlines():
        c = c.rstrip()
        res = re.search(reg, c)
        constrains.append(range(int(res[2]), int(res[3])+1))
        constrains.append(range(int(res[4]), int(res[5])+1))

        rules[res[1]] = constrains[-2:]

    valid_tickets = []
    for ticket_raw in nt[nt.index(":") + 2:].splitlines():
        ticket = [int(a) for a in ticket_raw.split(",")]
        ok = True
        for t in ticket:
            field_ok = False
            for c in constrains:
                if t in c:
                    field_ok = True
            if not field_ok:
                ok = False
        if ok:
            valid_tickets.append(ticket)

    col_len = len(valid_tickets[0])
    row_len = len(valid_tickets)

    graph = {}
    for name, constrains in rules.items():
        for c in range(col_len):
            valid = True
            for r in range(row_len):
                ticket_field = valid_tickets[r][c]
                field_ok = False
                for constrain in constrains:
                    if ticket_field in constrain:
                        field_ok = True
                if not field_ok:
                    valid = False
                    break
            if valid:
                graph[c] = graph.get(c, []) + [name]

    found = 0
    order = [False for _ in range(col_len)]
    while found < col_len:
        for c in range(col_len):
            possible = [i for i in graph[c] if i not in order]
            if len(possible) == 1:
                found += 1
                order[c] = possible[0]

    product = 1
    my_ticket = re.findall(r"\d+", mt)
    for i, o in enumerate(order):
        if "departure" in o:
            product *= int(my_ticket[i])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": product
        })
    }
