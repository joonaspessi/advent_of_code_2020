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


class Node(object):
    def __init__(self, parent, value, prev, next_):
        self.parent = parent
        self.value = value
        self.prev = prev
        self.next = next_

    def insert(self, value):
        node = Node(self.parent, value, self, self.next)
        self.parent.search_table[value] = node
        self.next = node
        node.next.prev = node
        return node

    def erase(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        del self.parent.search_table[self.value]


class LinkedList(object):
    def __init__(self):
        self.search_table = {}

    def append(self, prev, value):
        if prev is None:
            node = Node(self, value, None, None)
            node.next = node
            node.prev = node
            self.search_table[value] = node
            return node
        else:
            node = Node(self, value, prev, prev.next)
            prev.next = node
            node.next.prev = node
            self.search_table[value] = node
            return node

    def find(self, value):
        return self.search_table[value]


def lambda_handler_2(event, _):
    input = get_input(event)

    cups = [int(n) for n in input]
    llist = LinkedList()

    prev = None
    for c in cups:
        prev = llist.append(prev, c)

    next_value = 10
    while len(llist.search_table) < int(1e6):
        prev = llist.append(prev, next_value)
        next_value += 1

        if next_value % 10000 == 0:
            print(next_value)

    print(len(llist.search_table))
    assert next_value == int(1e6) + 1

    llist_len = len(llist.search_table)

    current_cup = llist.find(cups[0])

    for move in range(int(1e7)):
        if move % 1000 == 0:
            print(move)

        current_value = current_cup.value
        pick_up = []
        pick_uo_node = current_cup.next
        for _ in range(3):
            pick_up.append(pick_uo_node.value)
            tmp = pick_uo_node.next
            pick_uo_node.erase()
            pick_uo_node = tmp

        destination = current_value - 1 if current_value != 1 else llist_len

        while destination in pick_up:
            destination = destination - 1 if destination != 1 else llist_len

        destination_node = llist.find(destination)
        for n in pick_up:
            destination_node = destination_node.insert(n)

        current_cup = current_cup.next

    print("-- final --")
    node_1 = llist.find(1)
    print(node_1.next.value * node_1.next.next.value)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": node_1.next.value * node_1.next.next.value
        })
    }


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lambda_handler({"fileName": sys.argv[1]}, {})
    else:
        lambda_handler_2({"fileName": sys.argv[1]}, {})
