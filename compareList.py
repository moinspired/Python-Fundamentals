def compareList(list1, list2):
    checkEql = False
    message = "If they are not identical print"
    if len(list1) != len(list2):
        print message
    else:
        for i in range(0, len(list1)):
            if list1[i] == list2[i]:
                checkEql = True
            else:
                print message
        if checkEql == True:
            message = "The lists are the same"
            print message


list_one = [1, 2, 5, 6, 5]
list_two = [1, 2, 5, 6, 5]
compareList(list_one, list_two)
