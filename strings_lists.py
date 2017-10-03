#Find and replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace('day', 'month')


#min and max
x = [2, 54, -2, 7, 12, 98]
print max(x)
print min(x)


#first and last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[len(x) - 1]

# new list
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
y = x[0:len(x) / 2]
x = [y, 12, 98, 32, 10, -3, 6]
print x
