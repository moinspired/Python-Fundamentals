def findCharacters(list1, char):
    list2 = []
    if list1 == None:
        return null
    for i in list1:
        for characters in i:
            if characters == char:
                list2.append(i)
    print list2


word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
findCharacters(word_list, char)
