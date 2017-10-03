import random


def coinTosses():
    print "Starting the program..."
    head = 0
    tail = 0
    for i in range(0, 5):
        coin = int(round(random.random()))
        if coin == 1:
            head = head + 1
            print 'Attempt #' + str(i) + ': Throwing a coin... It\'s a head! ... Got ' + str(head) + ' head(s) so far and ' + str(tail) + ' tail(s) so far'
        elif coin == 0:
            tail = tail + 1
            print 'Attempt #' + str(i) + ': Throwing a coin... It\'s a head! ... Got ' + str(head) + ' head(s) so far and ' + str(tail) + ' tail(s) so far'


coinTosses()
