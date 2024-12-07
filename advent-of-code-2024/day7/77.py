import sys

from timeit import default_timer as timer
from pprint import pprint

import math
from itertools import product

def part1(filename):
    with open(filename, 'r') as fp:
        calcs = []
        size = 0
        for line in fp:
            parts = line.strip().split()
            calcs.append((int(parts[0][:-1]), [int(i) for i in parts[1:]]))
            size = max(size, len(parts)-1)
    
    valid = ('+', '*')
    answer = 0
    for target, digits in calcs:
        for ops in product(valid, repeat=len(digits)-1):
            val = digits[0]
            for op, i in zip(ops, digits[1:]):
                if op == '+':
                    val += i
                else:
                    val *= i
            
            if val == target:
                answer += target
                break

    print(f"Part 1: {answer}")
    return answer

def part2(filename):
    with open(filename, 'r') as fp:
        calcs = []
        size = 0
        for line in fp:
            parts = line.strip().split()
            calcs.append((int(parts[0][:-1]), [int(i) for i in parts[1:]]))
            size = max(size, len(parts)-1)
    
    valid = ('+', '*', '|')
    answer = 0
    for target, digits in calcs:  #.items():

        for ops in product(valid, repeat=len(digits)-1):
            val = digits[0]
            for op, i in zip(ops, digits[1:]):
                if op == '+':
                    val += i
                elif op == '*':
                    val *= i
                else:
                    val = int(str(val) + str(i))
                    # This is actually much slower...
                    # val = math.ceil(math.log10(val)) * 10 * val + i
            
            if val == target:
                answer += target
                break
    print(f"Part 2: {answer}")
    return answer

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <input file>", file=sys.stderr)
        sys.exit(1)

    before = timer()
    part1(sys.argv[1])
    after = timer()
    print(f"Part 1 Elapsed Time: {(after - before) * 1000.0:.6f} ms.")

    before = timer()
    part2(sys.argv[1])
    after = timer()
    print(f"Part 2 Elapsed Time: {(after - before) * 1000.0:.6f} ms.")

