#!/usr/bin/env python3

import random
import sys
import argparse


def main():
    words = 4
    numbers = 0
    symbols= 0
    caps = 0
    pswords = []
    usablesymbols = ["~", "!", "@", "#", "$", "%", "^", "*", "&", ":", ".", ";"]
    with open('/Users/andreajoshua/Desktop/words.txt') as c:

        wordslist = c.readlines()
        wordslist = [line.rstrip('\n') for line in open('/Users/andreajoshua/Desktop/words.txt')]
        parser = argparse.ArgumentParser()
        parser.add_argument("-w", "--words",
                         help="include WORDS words in the password (default=4)",
                            type=int, default=4)
        print("Adding words\n")

        parser.add_argument("-c", "--caps",
                           help="Capitalize CAPS random words in the password (default=0)",
                         type=int, default=0)
        print("Adding cap\n")

        parser.add_argument("-n", "--numbers",
                          help="insert NUMBERS random numbers in the password (default=0)",
                            type=int, default=0)
        print("Adding num\n")

        parser.add_argument("-s", "--symbols",
                             help="insert SYMBOLS random symbols in the password (default=0)",
                            type=int, default=0)
        print("Adding sym\n")
        args = parser.parse_args()
        if args.words != None:
            words = args.words
        if args.caps != None:
            caps = args.caps
        if args.numbers != None:
            numbers = args.numbers
        if args.symbols != None:
            symbols = args.symbols


        print(args.words)
        print(args.symbols)
        print(args.numbers)
        print(args.caps)

        for i in range(0, args.words):
            pswords.append(wordslist[random.randint(0, len(wordslist))])
            print("appending words\n")
        for j in range(0, args.caps):
            index = random.randint(0, words - 1)
            pswords[index] = pswords[index].capitalize()
            print("appending caps\n")
        for k in range(0, args.numbers):
            index = random.randint(0, words - 1)
            pswords[index] += str(random.randint(0, 9))
            print(''.join(pswords))
            print("appending nums\n")
        for l in range(0, args.symbols):
            index = random.randint(0, words - 1)
            symbols_index = random.randint(0, 11)
            pswords[index] += usablesymbols[symbols_index]
            print("appending symbols\n")
        print(''.join(pswords))


if __name__ == "__main__":
    main()
