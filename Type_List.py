"The list you entered is of mixed type"
arr1 = ['magical unicorns', 19, 'hello', 98.98, 'world']
arr2 = [2, 3, 1, 7, 4, 12]
arr3 = ['magical', 'unicorns']


def typeList(arr):
    stringVal = ""
    numVal = 0
    for i in arr:
        if type(i) is str:
            stringVal += i
            stringVal += " "
        if type(i) is int:
            numVal += i
    if not(stringVal is "") and not(numVal is 0):
        print "The list you entered is of mixed type"
    if stringVal is "" and not(numVal is 0):
        print "The list you entered is of integer type"
    if not(stringVal is "") and numVal is 0:
        print "The list you entered is of string type"
    if not(stringVal is 0):
        print stringVal
    if not(numVal is 0):
        print "Sum:", numVal


typeList(arr2)
