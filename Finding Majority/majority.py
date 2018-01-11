# Charles Buyas, cjb8qf, 10.24.17, majority.py

def majority(lstVals, equiv): #input is a list (lstVals) and a function (equiv) for checking equivalence of elements in the list. Do not change this function's signature.
    # we start with the assumption that there aren't any majority elements
    # we use equiv to compare to in order to find a majority element
    # we need to make sure that there is at least half of the elements equal to one value to ensure there is a majority
    # element, however there can be cases when there's an equal number of two different values
    # for example, if the list were [2, 2, 3, 3], then we technically have 2 majority elements.
    # we use the equiv to act as a sort of random num, and so that this case doesn't result in an error; instead of
    # as a function. This reduces the amount of work done at each step to reduce coefficients in asymptotic runtime
    totalNum = len(lstVals)
    if totalNum == 0:                       # if there aren't any values in the list, return equiv which starts at None
        return equiv
    compareList = []                        # make a second list to use for comparisons
    if totalNum % 2 == 1:                   # if there are an odd number of values, start off the equiv to the last element
        equiv = lstVals[-1]
    for i in range(0, totalNum-1, 2):       # for all of the values in the list
        if lstVals[i] == lstVals[i+1]:      # check to see if there are resulting copies of a value
            compareList.append(lstVals[i])  # append that repeated element to the new list
    biggun = majority(compareList, equiv)   # silly name for the element that's the major element to recurse
    if biggun is None:                      # basically pop out if empty
        return None
    newBiggun = lstVals.count(biggun)        # returns the number of occurrences of the biggun in the lstVals
    if 2*newBiggun > totalNum or (2*newBiggun == totalNum and biggun == equiv):   # checks to see if it's a majority, or equal to the tie breaker
        return biggun
    return None


#####################################
#you shouldn't need to change anything below here, if you do change something, make sure the I/O behavior remains unchanged.


def equals(x,y): #this function is given as the equiv argument to majority in main
    return x == y

def main():
    f = open('myvalues.txt', 'r') #opens a file named "myvalues.txt" as per instructions
    numVals = int(f.readline()) #the first line of the file gives the number of values in your list
    lstVals = [] #instantiate a list to contain the values
    for i in range(numVals):
        lstVals.append(int(f.readline())) #parse each value in the file as an int, insert into the list
    print(majority(lstVals,equals)) #prints the result of your algorithm, which should just be an int


main()
