#!/usr/bin/python

import itertools
import sys
import argparse

parser = argparse.ArgumentParser(description="Solve the n-queens problem.")
parser.add_argument("n", type=int, help="The size of the board and the amount of queens.")
args = parser.parse_args()
n = args.n

numberfound = 0

for poslist in itertools.permutations(range(n), n):
   tuples = list(enumerate(poslist))
   valid = True
   for (x1,y1),(x2,y2) in itertools.combinations(tuples,2):
      if x1 - x2 == y1 - y2 or x1 - y2 == x2 - y1:
         valid = False
         break
   if valid:
      numberfound += 1
      for i,q in enumerate(poslist):
         for j in range(n):
            if j == q:
               sys.stdout.write("><")
            elif (i-j)%2==0:
               sys.stdout.write("\u2591\u2591")
            else:
               sys.stdout.write("\u2592\u2592")
         sys.stdout.write("\n")
      sys.stdout.write("\n")
