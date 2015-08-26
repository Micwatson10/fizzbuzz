import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} arguments at run time".format(len(sys.argv))

for arg in sys.argv[1:]:
  print arg

n = int (arg) 
count = 1
while count < n+1:
    if (count%15) == 0: 
        print("fizzbuzz")
    elif (count%3) == 0:
        print("fizz")
    elif (count%5) == 0:
        print("buzz")
    else: 
        print(count)
    count = count + 1
        