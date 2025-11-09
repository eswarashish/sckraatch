# how to pass parameters through the console rather than through an input function

# eg. python3 myscript.py logfile.txt
# args and keyword args/ named params


def myfunc(*args,**kwargs):
    print(args[0])
    print(kwargs['age'])#kwargs is a dictionary

# to get the arguments passed through terminal we need to get the system arguments

import sys

filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'a') as f:
    f.write(message)
    f.close()



