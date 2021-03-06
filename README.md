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

Ensure that you have Python 3.8 installed and available in your environment.

Install and activate virtualenv

```
make venv
. .venv/bin/activate
```

and then run unit tests

```
make test
```

## Build and deploy API to AWS

For deployment, ensure that you have aws-sam-cli installed. For further
installation, please refer to official [instruction](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).

First build the project and then deploy with guided deployment

```
sam build && sam deploy --guided
```

After first guided deployment, you can use make shorthand

```
make deploy
```

## Day 1: Report Repair

Excercise testing skills to combine for loops. (Probably functional programmers would slap me due to this comment)

## Day 2: Password Philosophy

Excercise testing string parsing. Was easy to implement with regular expression.

## Day 3: Toboggan Trajectory

Excercise testing array indexing and modulo calculation

## Day 4: Passport Processing

Testing mostly input validation. Regex skills very useful

## Day 5: Binary Boarding

This excercise contained binary tree implementation in which I used recursive algorithm.
Second part was quite trivial two array comparison.

## Day 6: Custom Customs

Simple set operations including intersection

## Day 7: Handy Haversacks

Again interesting recursive implementation finding

## Day 8: Handheld Halting

Nice and simple assembler language runtime implementation.

## Day 9: Encoding Error

First excercise was straight forward. Simple array indexing.
In second excercise, I first understood the assignment wrong and made program that
tried to match four number sums. After actually READING the assignment properly,
the implementation was quite simple.

I still use enumerate-function for creating for loop with index. Still not sure that is
this the most Pythonic way of doing this...

## Day 10: Encoding Error

First excercise was simple after sorting the array to order. Basically just simple
array loop with right condition.

However, I didn't manage to get the second excercise done. I was missing memoization and
calculation would have taken too long. After doing some research, I ended up in a solution
where I builded graph for all the possible solutions. Basically the directed graph model contains
every adapter and its connected to next legal adapters which jolt is in the range of additonal 1-3 jolts.

Then by walking through all the permutations of this graph with using depth first search (DFS) algorithm
and memoization to store already calculated results gave me the right answer.

This was really good excercise to learn graph data modeling, DFS-algorithm and memoization

## Day 13: Shuttle Search

Second excercise contained problem that could be solved with [Chinese remainder
theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Computation)

## Day 18: Operation Order

First excercise was easy to implement by common logic. For the second excercise
I needed to start finding proper algorithm. Problem was solved with implementation of
[Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).

## Day 19: Monster Messages

This day was really hard to me get right. The correct answer was easily solved with
[CKY algorithm](https://en.wikipedia.org/wiki/CYK_algorithm). Algorithm solved both
parts 1 and 2. However, the execution time was really long, not sure if something wrong
with the implementation
