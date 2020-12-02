# copying from Reddit
# but it didn't work with stdin, so it wasn't worth it
# still nicer looking than my patterns

from typing import Iterator
#from sys import stdin

def read_input() -> Iterator[int]:
   f = open('modules')
   return map(int, list(f))

def fuel_required(mass: int) -> int:
   return mass // 3 -2

def total_fuel(mass: int) -> int:
   fuel = fuel_required(mass)
   return fuel + total_fuel(fuel) if fuel > 0 else 0

def part1():
   print(sum(map(fuel_required, read_input())))

def part2():
   print(sum(map(total_fuel, read_input())))

part1()

part2()
