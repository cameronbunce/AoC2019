def findCrosses(wires):
   # find intersections in map of two wires
   # walk the map looking for 'X'
   # make a list of intersection points ( tuples )
   crosses = []

   # for each point in one wire, see if it matches a the other wire
   for spota in wires[0]:
      for spotb in wires[1]:
         if spota == spotb:
            crosses.append(spota)
   return crosses

def shortestPath(intersections):
   # find the shortest path from origin to intersection point
   shortest = distance(intersections[0])
   for i in intersections:
      maybe = distance(i)
      if maybe < shortest:
         shortest = maybe
   return shortest

def distance(plot):
   x, y = plot
   return abs(x) + abs(y)

def mapMaker():
   # draw two lines with wire description
   # it seems silly to actually represent the whole mess
   # but rather to record coordinates for each line unit

   # ingest line descriptions

   # cheating for first tests
   """
   d1 = ('R75','D30','R83','U83','L12','D49','R71','U7','L72')
   d2 = ('U62','R66','U55','R34','D71','R55','D58','R83')

   d1 = ('R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51')
   d2 = ('U98','R91','D20','R16','D67','R40','U7','R15','U6','R7')
   """
   with open('wires') as f:
      d1 = f.readline().split(',')
      d2 = f.readline().split(',')
   return (plotter(d1),plotter(d2))


def plotter(plot):
   x = 0
   y = 0
   plots = []
   for direction in plot:
      point = direction[0]
      steps = int(direction[1:])
      if point == 'U':
         for i in range(steps):
            y += 1
            plots.append((x,y))
      elif point == 'D':
         for i in range(steps):
            y -= 1
            plots.append((x,y))
      elif point == 'L':
         for i in range(steps):
            x -= 1
            plots.append((x,y))
      elif point == 'R':
         for i in range(steps):
            x += 1
            plots.append((x,y))
      else:
         print("oops")
         break
   return plots


print(shortestPath(findCrosses(mapMaker())))
