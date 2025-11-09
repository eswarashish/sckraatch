# usage: python main.py logfile.txt
## Optional orgs

import getopt,sys

opts, args = getopt.getopt(sys.argv[1:],# this means accept everything except the first arg
                           "f:m:",# these are the optional args we can pass as -f and -m
                           ['filename','message']   )

print(opts)
print(args)

# case 1: python optional_args.py loglife.txt "Hello" --> zero optional args
# case 2: python optional_args.py -f logfile.txt -m "Hello" -->f, m optionals args defined

#datacollection from args
filename = sys.argv[1],
#.... for optional ones

for opt, arg in opts:
    if opt == '-f':
        filename = arg,
    if opt == '-m':
        message = arg