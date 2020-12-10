from functools import lru_cache
import json
import itertools


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day5/input.txt", 'r') as f:
            lines = f.readlines()

    adapters = [int(line) for line in lines]
    adapters.sort()
    return adapters


def is_valid_set(adapters, output_jolt):
    adapt = adapters[:]
    adapt.insert(0, 0)
    adapt.append(output_jolt)
    for index, adapter in enumerate(adapt):
        if index + 1 == len(adapters):
            break
        if adapt[index + 1] - adapter > 3:
            return False
    return True


def lambda_handler(event, _):
    """Advent of code day 10, excercise 1
    """
    adapters = get_input(event)
    diff_1 = 0
    diff_3 = 0
    for index, adapter in enumerate(adapters):
        if index == 0:
            diff_1 += (1 if adapters[index] <= 2 else 0)
            diff_3 += 1 if adapters[index] == 3 else 0

        if index + 1 == len(adapters):
            diff_3 += 1
            break

        if adapters[index + 1] - adapter == 1:
            diff_1 += 1

        if adapters[index + 1] - adapter == 3:
            diff_3 += 1

        if adapters[index + 1] - adapter > 3:
            raise Exception("missing neccessary adapters")

    result = diff_1 * diff_3

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        }),
    }


def make_graph(data):
    graph = {}
    data = [0] + data
    for i, x in enumerate(data):
        graph[x] = [y for y in data[i + 1:i + 4] if 0 < y - x <= 3]
    graph[max(data)] = [max(data) + 3]
    return graph


def lambda_handler_2(event, _):
    """Advent of code day 9, excercise 2
    """
    adapters = get_input(event)
    graph = make_graph(adapters)

    @lru_cache(None)
    def dfs(node):
        print(node)
        if node not in graph.keys():
            return 1
        return sum(dfs(nnode) for nnode in graph[node])
    result = dfs(0)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        }),
    }
