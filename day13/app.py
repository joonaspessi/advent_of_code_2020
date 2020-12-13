import json
from functools import reduce


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day12/input.txt", 'r') as f:
            lines = f.readlines()
    return [line for line in lines]


def mod_pow(b, e, mod):
    if e == 0:
        return 1
    elif e % 2 == 0:
        return mod_pow((b*b) % mod, e/2, mod)
    else:
        return (b*mod_pow(b, e-1, mod)) % mod


def invert_modulo(a, m):
    return mod_pow(a, m-2, m)


def gcd(x, y):
    """ Greates commond divisor
        >>>> For example, the gcd of 8 and 12 is 4, gcd(8,12) == 1
    """
    if x == 0:
        return y
    return gcd(y % x, x)


def lambda_handler(event, _):
    input = get_input(event)
    time = int(input[0])
    lines = input[1].replace(",x", "").split(",")
    lines = list(map(lambda n: int(n), lines))
    lines.sort()

    original_time = time
    wait_time = 0
    result_line = -1
    while True:
        for line in lines:
            if time % line == 0:
                result_line = line
                wait_time = time - original_time
                break
        if result_line != -1:
            break

        time += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result_line * wait_time
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    lines = list(filter(lambda n: n[1] != "x", [
                 (index, line) for index, line in enumerate(input[1].split(","))]))
    lines = list(map(lambda n: (n[0], int(n[1])), lines))

    # (T + i) % line == 0
    # ==> (line - i) % line
    constrains = []
    N = 1
    for i, line in lines:
        i %= line
        constrain = (line - i) % line
        constrains.append((constrain, line))
        N *= line

    ans = 0
    for i, l in constrains:
        ni = int(N/l)
        assert gcd(ni, l) == 1
        mi = int(invert_modulo(ni, l))
        assert (mi * ni) % l == 1
        assert (i * mi * ni) % l == i
        res = i * mi * ni
        assert res % l == i
        assert res % ni == 0
        ans += res

    result = ans % N
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
