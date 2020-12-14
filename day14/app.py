import json
from functools import reduce


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day12/input.txt", 'r') as f:
            lines = f.readlines()
    return lines


def set_mem(val, mask):
    for i, b in enumerate(list(reversed(mask))):
        if b == "0":
            val = val & ~(1 << i)
        elif b == "1":
            val = val | (1 << i)
    return val


def get_cmds(input):
    cmds = []
    for i in input:
        if i.startswith("mask"):
            op = "mask"
            cmd = i[7:]
        else:
            op = "mem"

            cmd = [i[i.find("[")+1: i.find("]")], i[i.find("=")+2:]]
        cmds.append((op, cmd))
    return cmds


def lambda_handler(event, _):
    input = get_input(event)
    cmds = get_cmds(input)

    mask = ""
    mem = {}
    for c in cmds:
        if c[0] == "mask":
            mask = c[1]
        elif c[0] == "mem":
            mem[c[1][0]] = set_mem(
                int(c[1][1]), mask)
        else:
            assert False

    result = sum([m for m in mem.values()])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def permute(arr, l, r):
    res = []
    if l == r:
        return arr
    else:
        if arr[l] != "X":
            permute(arr, l+1, r)
        else:
            for i in [0, 1]:
                temp = arr[:]
                temp[l] = i
                permute(temp, l+1, r)


def get_addr(addr, mask):
    a = [int(b) for b in (bin(int(addr))[2:])]
    l = []
    for i in range(36 - len(a)):
        l.append(0)
    a = l + a
    for i, b in enumerate(mask):
        if b == "0" or b == "1":
            b = int(b)
            a[i] = b or int(a[i])
            a[i] = str(a[i])
        elif b == "X":
            a[i] = "X"

    permutations = []

    def permute(arr, l, r):
        if l == r:
            permutations.append(arr)
            return
        else:
            if arr[l] != "X":
                permute(arr, l+1, r)
            else:
                for i in ["0", "1"]:
                    temp = arr[:]
                    temp[l] = i
                    permute(temp, l+1, r)
    permute(a[:], 0, len(a))
    return [int("".join(n), 2) for n in permutations]


def lambda_handler_2(event, _):
    input = get_input(event)
    cmds = get_cmds(input)

    mask = ""
    mem = {}
    for c in cmds:
        if c[0] == "mask":
            mask = c[1]
        elif c[0] == "mem":
            addrs = get_addr(c[1][0], mask)
            for addr in addrs:
                mem[addr] = int(c[1][1])
        else:
            assert False

    result = sum([m for m in mem.values()])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
