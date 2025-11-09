# generators does lazy executions
def mygeneratior(x):
    # we are not going to retur in a normal way except we are going to use yield
    yield x ** 3 #cube

values = mygeneratior(90000)
print(values)# generator returns a generator object an iterator

print(next(values))# only when called that particular execution happens... so  it save a lot of computation and spoace for different scenarios
# so untill and unless you use the next keyword exectution doesnot happen this is called as lazy execution
# u can also do this with iteration
# so this doesnot hold a list with all the values before hand exedcuted until u ask for one
for x in values:
    print(x)