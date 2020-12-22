import json
import sys


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def get_players(input):
    player_inputs = input.split("\n\n")
    players = []
    for p in player_inputs:
        players.append([int(card) for card in p.splitlines()[1:]])
    return (players[0], players[1])


def get_deck_score(deck):
    score = 0
    for i, card in enumerate(reversed(deck)):
        score += (i+1) * card
    return score


def get_winner(p1, p2):
    if len(p1) == 0:
        return (1, p2)
    else:
        return (0, p1)


def play_game(p1, p2, game=1, round=1, part2=False):
    print("")
    print(f"=== Game {game} ===")

    current_game = game
    played_hands_p1 = []
    played_hands_p2 = []

    while len(p1) > 0 and len(p2) > 0:
        print("")
        print(f"-- Round {round} (Game {current_game}) --")
        print(f"Player 1's deck: {p1}")
        print(f"Player 2's deck: {p2}")

        if part2:
            # Check if should end the game early to avoid recursion
            if p1 in played_hands_p1 or p2 in played_hands_p2:
                return (0, p1, game)

            # store played hands
            played_hands_p1.append(p1[:])
            played_hands_p2.append(p2[:])

        # draw cards
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        print(f"Player 1 plays: {c1}")
        print(f"Player 2 plays: {c2}")

        # check if should play sub-game (part2) or end the round
        if len(p1) >= c1 and len(p2) >= c2 and part2:
            print("Playing a sub-game to determine the winner...")
            game += 1
            winner, _, game = play_game(p1[0:c1], p2[0:c2], game, 1, part2)
            print("")
            print(f"...anyway, back to game {current_game}")
        elif c1 > c2:
            winner = 0
        else:
            winner = 1

        # round winner procdedures
        if winner == 0:
            print(f"Player 1 wins the round {round} of game {current_game}!")
            p1.extend([c1, c2])
        else:
            print(f"Player 2 wins the round {round} of game {current_game}!")
            p2.extend([c2, c1])

        round += 1
    winner, win_deck = get_winner(p1, p2)
    return (winner, win_deck, game)


def lambda_handler(event, _):
    input = get_input(event)
    players = get_players(input)
    p1, p2 = players
    _, deck, _ = play_game(p1, p2, 1, 1, part2=False)
    result = get_deck_score(deck)
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    players = get_players(input)
    p1, p2 = players
    _, deck, _ = play_game(p1, p2, 1, 1, part2=True)
    result = get_deck_score(deck)
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) == 2:
        lambda_handler({"fileName": sys.argv[1]}, {})
    else:
        lambda_handler_2({"fileName": sys.argv[1]}, {})
