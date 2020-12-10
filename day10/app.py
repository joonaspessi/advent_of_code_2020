from functools import lru_cache
import json
import itertools


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day10/input.txt", 'r') as f:
            lines = f.readlines()

    adapters = [int(line) for line in lines]
    adapters.sort()
    return adapters


def make_graph(adapters):
    graph = {}
    adapters = [0] + adapters
    for index, adapter in enumerate(adapters):
        graph[adapter] = [
            next for next in adapters[index + 1:index + 4] if 0 < next - adapter <= 3]
    graph[max(adapters)] = [max(adapters) + 3]
    return graph


def lambda_handler(event, _):
    """Advent of code day 10, excercise 1
    """
    adapters = get_input(event)
    adapters = [0] + adapters + [max(adapters) + 3]

    diff_1 = 0
    diff_3 = 0
    for index, adapter in enumerate(adapters):
        if index + 1 == len(adapters):
            break
        if adapters[index + 1] - adapter == 1:
            diff_1 += 1
        if adapters[index + 1] - adapter == 3:
            diff_3 += 1
    result = diff_1 * diff_3

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        }),
    }


def lambda_handler_2(event, _):
    """Advent of code day 10, excercise 2
    """
    adapters = get_input(event)
    graph = make_graph(adapters)

    @lru_cache(None)
    def dfs(node):
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
