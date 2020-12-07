# Advent of Code 2020

[adventofcode.com](https://adventofcode.com/) implementation in Python 3 with Serverless twist.
All challenges are implemented as AWS Lambdas and published via AWS API Gateway.
Deployment is done using AWS SAM.

Answer to each excercise can be POSTED to API endpoint that follows pattern

```
curl -X POST \
--data-binary "@day${day_number}/input.txt" \
"https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day${day_number}/${excercise_number}"

```

Where ${day_number} is number of day ranging 1-25 and ${excercise_number} is excercise number ranging 1-2

## Development environment

TODO

- How to create venv
- How to run unit tests

## Deployment

TODO

- How to build sam
- How to deploy sam

## Day 1

Excercise testing skills to combine for loops. (Probably functional programmers would slap me due to this comment)

```
curl -X POST \
--data-binary '@day1/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day1/1

curl -X POST \
--data-binary '@day1/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day1/2
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

### Day 4

Testing mostly input validation. Regex skills very useful

```
curl -X POST \
--data-binary '@day4/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day4/1

curl -X POST \
--data-binary '@day4/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day4/2
```

### Day 5

This excercise contained binary tree implementation in which I used recursive algorithm.
Second part was quite trivial two array comparison.

```
curl -X POST \
--data-binary '@day5/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day5/1

curl -X POST \
--data-binary '@day5/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day5/2
```

### Day 6

Simple set operations including intersection

```
curl -X POST \
--data-binary '@day6/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day6/1

curl -X POST \
--data-binary '@day6/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day6/2
```

### Day 7: Handy Haversacks

Again interesting recursive implementation finding

```
curl -X POST \
--data-binary '@day7/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day7/1

curl -X POST \
--data-binary '@day7/input.txt' \
https://8f0dqkl1q6.execute-api.eu-west-1.amazonaws.com/Prod/day7/2
```
