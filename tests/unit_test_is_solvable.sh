#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
rm -rf tests_generated ; mkdir tests_generated
for i in {3..5}
do
  mkdir tests_generated/"$i"-puzzle
  for j in {0..30}
  do
    python3 generator_test.py $i > tests_generated/"$i"-puzzle/"$j"-test
    my_result=$(python3 ./npuzzle.py -f tests_generated/"$i"-puzzle/"$j"-test -he "linear_conflict" | grep -o -m1 "unsolvable")
    result=$(grep -o "unsolvable" ./tests_generated/"$i"-puzzle/"$j"-test)
    if [ "$my_result" != "$result" ]; then
       echo ${RED}tests_generated/"$i"-puzzle/"$j"-test${NC}
    else
      echo ${GREEN}tests_generated/"$i"-puzzle/"$j"-test${NC}
    fi
  done
done
