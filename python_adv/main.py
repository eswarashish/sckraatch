# python is a dynamic and not a staticly typed language 
# which mean we dont know the data types until runtime
# so type hinting is used ; where type is hinted for developement but not strictly enforced 
def myfunction(myparameter: int):
    print(myparameter)

# this will enable myparameter to have int properties so we can develop
# but still myparameter can be anything
# eg: myfunction("Hello")  works!! since this is just type hinting
