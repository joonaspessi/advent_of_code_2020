# Advent of Code 2020

[adventofcode.com](https://adventofcode.com/) implementation in Python 3 with Serverless twist.
All challenges are implemented as AWS Lambdas and published via AWS API Gateway.
Answer to each excercise can POSTED to API endpoint that follows pattern

```
https://<api_base_url>/day<x>/<y>, where x is day number ranging 1-25 and y is excercise number ranging 1-2
```

## Day 1

Excercise testing skills to combine for loops. (Probably functional programmers would slap me due to this comment)

```
curl -X POST \
-d '{"report": [1721, 979, 366, 299, 675, 1456]}' \
https://xxxxxxxxxx.execute-api.eu-west-1.amazonaws.com/Prod/day1/1

curl -X POST \
-d '{"report": [1721, 979, 366, 299, 675, 1456]}' \
https://xxxxxxxxxx.execute-api.eu-west-1.amazonaws.com/Prod/day1/2
```

### Day 2

Excercise testing string parsing. Was easy to implement with regular expression.

```
curl -X POST \
-d '{"input": ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]}' \
https://xxxxxxxxxx.execute-api.eu-west-1.amazonaws.com/Prod/day2/1

curl -X POST \
-d '{"input": ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]}' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day2/2
```

### Day 3

Excercise testing array indexing and modulo calculation

```
curl -X POST \
-d '{"input": ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]}' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day3/1

curl -X POST \
-d '{"input": ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]}' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day3/2
```
