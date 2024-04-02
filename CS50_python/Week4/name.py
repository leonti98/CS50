import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("too many arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

#print name tag

