# for each module,
# take the mass, divide by 3, rounding down and subtract two
# add total of fuel for all modules
import math

with open('modules') as f:
   masses = list(f)
fuel = 0
for mass in masses:
   onefuel = 0
   try:
      onefuel = math.floor(int(mass)/3)-2
   except TypeError:
      pass
   except ValueError:
      pass
#   print("starting fuel "+str(fuel)+" mass "+str(mass)+" fuel this stage "+str(onefuel))
   fuel += onefuel
print(fuel)
