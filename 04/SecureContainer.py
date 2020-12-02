def pair(password):
   for i in range(5):
      if (password[i] == password[i+1]):
         print(password+" pair found ", end="")
         return True
   return False

def three(password):
   for i in range(4):
      if password[i] == password[i+1] == password[i+2]:
         print(" three found ")
         return True
   print(" not three found ", end="")
   return False

def four(password):
   for i in range(3):
      if password[i] == password[i+1] == password[i+2] == password[i+3]:
         print(" four found ")
         return True
   print(" not four found ", end="")
   return False

def climbing(password):
   for i in range(5):
      if password[i] > password[i+1]:
         print("not climbing")
         return False
   print("climbing")
   return True

solutions = []
#for x in [112233,123444,111122]:
for x in range(256310, 732736):
   test = str(x)
   if climbing(test):
      if not four(test):
         if not three(test):
            if pair(test):
               solutions.append(test)

print(len(solutions))


