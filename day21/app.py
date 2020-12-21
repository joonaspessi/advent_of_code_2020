import json
import sys
import fileinput
from collections import defaultdict


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)

    all_ingredients = set()
    all_allergens = set()
    foods = []

    for line in input.splitlines():
        first, rest = line.split("(contains ")
        ingredients = set(first.split())
        allergens = set(rest[:-1].split(", "))
        all_ingredients |= ingredients
        all_allergens |= allergens
        foods.append((ingredients, allergens))

    # ingredient -> allergen
    ingredient_to_allergen = {
        ingredient: set(all_allergens) for ingredient in all_ingredients}
    ingredient_count = defaultdict(int)

    for i, a in foods:
        for ingredient in i:
            ingredient_count[ingredient] += 1

        for aa in a:
            for ii in all_ingredients:
                if ii not in i:
                    ingredient_to_allergen[ii].discard(aa)

    result = 0
    for i in all_ingredients:
        if not ingredient_to_allergen[i]:
            result += ingredient_count[i]

    print(result)
    print(ingredient_to_allergen)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


if __name__ == "__main__":
    lambda_handler({"fileName": sys.argv[1]}, {})
