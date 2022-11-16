from statistics import mean


def avg(x, y):
    average = (x) / 2
    next = float(y) / 2
    return average, next
 
x = 128
y = 255
z = avg (x,y)
print ("The average of",x,"and", y, "is", z)
