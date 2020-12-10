import json
import math


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day7/input.txt", 'r') as f:
            lines = f.readlines()
    return lines


def parse_input(input_lines):
    def parse_inner(inner_input):
        return {
            "amount": inner_input[:1],
            "name": inner_input[2:]
        }

    bags = {}
    for line in input_lines:
        parsed = line.replace(" bags contain ", ":").replace(
            " bag, ", ":").replace(" bags, ", ":").replace(" bags.", "").replace(" bag.", "").split(":")
        bag_name = parsed[0]
        bag_inner = filter(lambda n: n != "no other", parsed[1:])
        bags[bag_name] = {
            "inner": list(map(parse_inner, bag_inner))
        }
    print(bags)
    return bags


def can_contain_gold(bag, bags, checked_bags):
    if bag in checked_bags:
        return False

    checked_bags.append(bag)

    if bag == "shiny gold":
        return True

    inner_bags = [inner_bag["name"] for inner_bag in bags[bag]["inner"]]

    has_gold_in_inner = len(
        list(filter(lambda n: n == "shiny gold", inner_bags))) > 0

    if has_gold_in_inner:
        return True

    for inner_bag in inner_bags:
        if can_contain_gold(inner_bag, bags, checked_bags):
            return True

    return False


def required_bags(bag, bags, amount):

    inner_bags = [inner_bag["name"] for inner_bag in bags[bag]["inner"]]

    for inner_bag in bags[bag]["inner"]:
        amount += int(inner_bag["amount"])
        amount += int(inner_bag["amount"]) * \
            required_bags(inner_bag["name"], bags, 0)

    return amount


def lambda_handler(event, _context):
    """Advent of code day 7, excercise 1
    """
    input_lines = get_input(event)
    bags = parse_input(input_lines)

    can_contain = 0
    for bag in bags:
        if bag == "shiny gold":
            continue
        if can_contain_gold(bag, bags, []):
            can_contain += 1
            print(f"{bag} can contain gold")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": can_contain
        }),
    }


def lambda_handler_2(event, _context):
    """Advent of code day 7, excercise 2
    """
    input_lines = get_input(event)
    bags = parse_input(input_lines)
    bags_required = required_bags("shiny gold", bags, 0)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": bags_required
        }),
    }
